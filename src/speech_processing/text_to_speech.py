import os
from dotenv import load_dotenv
from deepgram import DeepgramClient
import pygame
import time
import threading

load_dotenv()

class TTS:
    def __init__(self):
        self.filename = "output.wav"
        self.interrupted = threading.Event()  # Interruption flag
        
        # Initialize pygame mixer with specific settings for Windows
        try:
            pygame.mixer.quit()  # Quit any existing mixer
        except:
            pass
        
        try:
            # Initialize with specific frequency that matches Deepgram output
            pygame.mixer.init(frequency=16000, size=-16, channels=1, buffer=512)
            print("[TTS] Pygame mixer initialized successfully")
        except Exception as e:
            print(f"[TTS Warning] Pygame init issue: {e}")
    
    def interrupt(self):
        """Stop the current speech immediately"""
        self.interrupted.set()
        try:
            pygame.mixer.music.stop()
            print("[TTS] Speech interrupted!")
        except:
            pass
    
    def speak(self, text, interruption_flag=None):
        if not text or len(text.strip()) == 0:
            print("[TTS] No text to speak")
            return
        
        # Reset interruption flag
        self.interrupted.clear()
        
        # Use external flag if provided, otherwise use internal
        interrupt_check = interruption_flag if interruption_flag else self.interrupted
            
        try:
            print(f"[TTS] Generating speech for: {text[:50]}...")
            
            # STEP 1: Create a Deepgram client
            deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

            # STEP 2: Generate audio
            response = deepgram.speak.v1.audio.generate(
                text=text,
                model="aura-asteria-en",
                encoding="linear16",
                sample_rate=16000
            )

            # STEP 3: Save the audio to a file
            # The response is a generator that yields audio chunks
            audio_data = b""
            for chunk in response:
                # Check for interruption during generation
                if interrupt_check.is_set():
                    print("[TTS] Interrupted during audio generation")
                    return
                audio_data += chunk
            
            print(f"[TTS] Audio generated: {len(audio_data)} bytes")
            
            with open(self.filename, "wb") as audio_file:
                audio_file.write(audio_data)
            
            print(f"[TTS] Audio saved to {self.filename}")

            # STEP 4: Play the audio file using pygame
            try:
                # Reinitialize mixer to ensure clean state
                pygame.mixer.quit()
                pygame.mixer.init(frequency=16000, size=-16, channels=1, buffer=512)
                
                # Load and play
                pygame.mixer.music.load(self.filename)
                pygame.mixer.music.play()
                
                print("[TTS] Playing audio... (Press SPACE to interrupt)")
                
                # Wait for playback to finish OR interruption
                while pygame.mixer.music.get_busy():
                    # Check for interruption every 100ms
                    if interrupt_check.is_set():
                        pygame.mixer.music.stop()
                        print("[TTS] Playback interrupted by user!")
                        return
                    pygame.time.Clock().tick(10)
                    time.sleep(0.1)
                
                print("[TTS] Playback complete")
                
            except Exception as play_error:
                print(f"[TTS Error] Playback failed: {play_error}")
                print(f"[TTS] Audio file saved as '{self.filename}' - you can play it manually")

        except Exception as e:
            print(f"[TTS Error] Exception: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    tts = TTS()
    tts.speak("Hello, how can I help you today?")
