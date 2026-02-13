import asyncio
import os
from dotenv import load_dotenv
from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.extensions.types.sockets import ListenV1SocketClientResponse, ListenV1MediaMessage, ListenV1ControlMessage
import pyaudio

# Load environment variables from a .env file
load_dotenv()

class TranscriptCollector:
    def __init__(self):
        self.reset()

    def reset(self):
        # Initialize or reset the transcript parts list
        self.transcript_parts = []

    def add_part(self, part):
        # Add a part of the transcript to the list
        self.transcript_parts.append(part)

    def get_full_transcript(self):
        # Join all parts of the transcript into a single string
        return ' '.join(self.transcript_parts)

# Create an instance of TranscriptCollector to manage transcript parts
transcript_collector = TranscriptCollector()

async def get_transcript(callback):
    # Event to signal transcription completion
    transcription_complete = asyncio.Event()
    should_stop_streaming = False

    try:
        # Initialize Deepgram client with API key from environment
        deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

        # Initialize a connection to Deepgram's websocket API v1
        with deepgram.listen.v1.connect(
            model="nova-2",
            punctuate=True,
            language="en-US",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            endpointing=300,
            smart_format=True,
        ) as dg_connection:
            
            print("\n=== Ready to listen ===")
            print("Speak now, then pause. The system will detect when you're done.\n")

            def on_message(message: ListenV1SocketClientResponse) -> None:
                nonlocal should_stop_streaming
                
                # Check if this is a transcript event with channel data
                if hasattr(message, 'channel') and hasattr(message.channel, 'alternatives'):
                    # Extract the transcript from the result
                    sentence = message.channel.alternatives[0].transcript
                    
                    # Check if this is a final result
                    speech_final = getattr(message, 'speech_final', False)
                    
                    if not speech_final:
                        # Add interim results to the transcript collector
                        transcript_collector.add_part(sentence)
                    else:
                        # Add the final part of the current sentence to the transcript collector
                        transcript_collector.add_part(sentence)
                        # Get the full sentence from the transcript collector
                        full_sentence = transcript_collector.get_full_transcript()
                        # Check if the full sentence is not empty before printing
                        if len(full_sentence.strip()) > 0:
                            full_sentence = full_sentence.strip()
                            print(f"Human: {full_sentence}")
                            # Call the callback with the full sentence
                            callback(full_sentence)
                            # Reset the transcript collector for the next sentence
                            transcript_collector.reset()
                            
                            # Signal to stop streaming and close connection
                            should_stop_streaming = True
                            
                            # Send Finalize control message to Deepgram
                            try:
                                dg_connection.send_control(ListenV1ControlMessage(type="Finalize"))
                            except:
                                pass  # Connection might already be closing
                            
                            # Signal completion
                            asyncio.get_event_loop().call_soon_threadsafe(
                                transcription_complete.set
                            )

            # Set up the event listeners
            dg_connection.on(EventType.OPEN, lambda _: print("[Microphone Active - Start Speaking]"))
            dg_connection.on(EventType.MESSAGE, on_message)
            dg_connection.on(EventType.CLOSE, lambda _: print("[Transcription Complete - Processing...]\n"))
            dg_connection.on(EventType.ERROR, lambda error: None)  # Suppress keepalive errors during shutdown

            # Start listening in a background task
            import concurrent.futures
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            future = executor.submit(dg_connection.start_listening)

            # Set up PyAudio for microphone input
            CHUNK = 8192
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 16000

            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
            )

            # Stream audio from microphone to Deepgram
            try:
                while not transcription_complete.is_set() and not should_stop_streaming:
                    data = stream.read(CHUNK, exception_on_overflow=False)
                    # Send audio using the correct message type
                    try:
                        dg_connection.send_media(ListenV1MediaMessage(data))
                    except:
                        # Connection might be closing
                        break
                    await asyncio.sleep(0.01)  # Small delay to prevent busy waiting
            except Exception as e:
                pass  # Suppress errors during shutdown
            finally:
                # Clean up audio stream immediately
                stream.stop_stream()
                stream.close()
                audio.terminate()
                
                # Give a moment for the Finalize message to be processed
                await asyncio.sleep(0.1)

    except Exception as e:
        print(f"Could not open socket: {e}")
        return

# Global variable to store the transcription response
transcription_response = ""

def handle_full_sentence(full_sentence):
    global transcription_response
    transcription_response = full_sentence

if __name__ == "__main__":
    # Run the get_transcript function and pass handle_full_sentence as the callback
    asyncio.run(get_transcript(handle_full_sentence))