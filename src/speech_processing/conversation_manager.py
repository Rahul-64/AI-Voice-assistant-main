from .speech_to_text import get_transcript
from .text_to_speech import TTS
import time
import threading
from pynput import keyboard


class ConversationManager:
    def __init__(self, assistant):
        self.transcription_response = ""
        self.assistant = assistant
        self.interrupt_flag = threading.Event()
        self.keyboard_listener = None

    def on_key_press(self, key):
        """Handle keyboard interrupt"""
        try:
            # Check if SPACE key is pressed
            if key == keyboard.Key.space:
                print("\n[!] SPACE pressed - Interrupting AI...")
                self.interrupt_flag.set()
        except AttributeError:
            pass

    def start_keyboard_listener(self):
        """Start listening for keyboard interrupts"""
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()

    def stop_keyboard_listener(self):
        """Stop the keyboard listener"""
        if self.keyboard_listener:
            self.keyboard_listener.stop()

    async def main(self):
        def handle_full_sentence(full_sentence):
            self.transcription_response = full_sentence

        print("\n" + "="*60)
        print("AI VOICE ASSISTANT - Simple Chat Mode")
        print("="*60)
        print("Instructions:")
        print("  1. Speak clearly when prompted")
        print("  2. Pause when done speaking (system auto-detects)")
        print("  3. Wait for AI response")
        print("  4. Press SPACE to interrupt AI while speaking")
        print("  5. Say 'goodbye' to exit")
        print("="*60 + "\n")

        # Start keyboard listener
        self.start_keyboard_listener()
        print("[Keyboard listener active - SPACE to interrupt]\n")

        try:
            # Loop indefinitely until "goodbye" is said
            while True:
                await get_transcript(handle_full_sentence)
                
                # Check for "goodbye" to exit the loop
                if "goodbye" in self.transcription_response.lower():
                    print("\n[Goodbye! Shutting down...]")
                    break
                
                # Start timing the AI response
                print("[AI is thinking...]")
                start_time = time.time()
                
                llm_response = self.assistant.invoke(self.transcription_response)
                
                end_time = time.time()
                processing_time = end_time - start_time
                print(f"\nAI: {llm_response}")
                print(f"[Processing took {processing_time:.2f} seconds]\n")

                # Clear interrupt flag before speaking
                self.interrupt_flag.clear()
                
                print("[Speaking response...]")
                tts = TTS()
                tts.speak(llm_response, interruption_flag=self.interrupt_flag)
                
                # Check if interrupted
                if self.interrupt_flag.is_set():
                    print("[AI speech was interrupted - Ready for new input]\n")
                    self.interrupt_flag.clear()

                # Reset transcription_response for the next loop iteration
                self.transcription_response = ""
        
        finally:
            # Clean up keyboard listener
            self.stop_keyboard_listener()
            print("\n[Keyboard listener stopped]")