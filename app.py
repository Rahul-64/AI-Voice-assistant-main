import streamlit as st
import asyncio
from src.agents.agent import Agent
from src.speech_processing.text_to_speech import TextToSpeech
import os
from dotenv import load_dotenv
import io
from litellm import completion
import base64

load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎤",
    layout="centered"
)

# Simple CSS for minimal styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'agent' not in st.session_state:
    model = "groq/llama-3.3-70b-versatile"
    simple_prompt = """You are a helpful and friendly AI voice assistant.

Your personality:
- Friendly and conversational
- Helpful and informative
- Clear and concise in responses
- Patient and understanding

Guidelines:
- Keep responses brief (2-3 sentences max)
- Be natural and conversational
- Provide helpful information when asked
- Stay on topic and focused
- Be respectful and polite

Keep your responses concise and conversational (2-3 sentences).
"""
    st.session_state.agent = Agent("Voice Assistant", model, tools=[], system_prompt=simple_prompt)

# Header
st.markdown("<h1 class='main-header'>🎤 AI Voice Assistant</h1>", unsafe_allow_html=True)
st.markdown("---")

# Check API keys
deepgram_key = os.getenv("DEEPGRAM_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")

if not deepgram_key or not groq_key:
    st.error("⚠️ API keys not found!")
    st.info("""
    Please set your API keys:
    1. Create a `.env` file in the project root
    2. Add:
       - DEEPGRAM_API_KEY=your_key_here
       - GROQ_API_KEY=your_key_here
    
    Or set them in Streamlit Cloud Secrets.
    """)
    st.stop()

# Input method selection
st.subheader("Choose Input Method")
input_method = st.radio("", ["Text Input", "Voice Input (Coming Soon)"], label_visibility="collapsed")

# Text input mode
if input_method == "Text Input":
    user_input = st.text_input("Your message:", placeholder="Type your message here...")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        send_button = st.button("Send", type="primary")
    with col2:
        clear_button = st.button("Clear Chat")
    
    if clear_button:
        st.session_state.conversation_history = []
        st.rerun()
    
    if send_button and user_input:
        # Add user message to history
        st.session_state.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Get AI response
        with st.spinner("AI is thinking..."):
            try:
                response = st.session_state.agent.process_request(user_input)
                
                # Add AI response to history
                st.session_state.conversation_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Generate audio
                tts = TextToSpeech()
                audio_bytes = tts.generate_speech(response)
                
                if audio_bytes:
                    st.session_state.last_audio = audio_bytes
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.rerun()

# Display conversation history
if st.session_state.conversation_history:
    st.markdown("---")
    st.subheader("Conversation")
    
    for message in st.session_state.conversation_history:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**AI:** {message['content']}")
            
    # Play last audio if available
    if hasattr(st.session_state, 'last_audio') and st.session_state.last_audio:
        st.audio(st.session_state.last_audio, format='audio/wav')

# Voice input placeholder
else:
    st.info("Voice recording will be available when deployed. For now, use text input.")
    st.markdown("""
    ### Features:
    - 🤖 AI-powered conversations
    - 🔊 Text-to-speech responses
    - 💬 Text chat interface
    - 🎯 Simple and easy to use
    """)

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("AI Voice Assistant powered by:")
    st.write("- Groq (Llama 3.3 70B)")
    st.write("- Deepgram (TTS)")
    
    st.markdown("---")
    
    st.header("Instructions")
    st.write("1. Type your message")
    st.write("2. Click Send")
    st.write("3. AI responds with text and voice")
    
    st.markdown("---")
    
    if st.button("Clear All"):
        st.session_state.conversation_history = []
        if hasattr(st.session_state, 'last_audio'):
            del st.session_state.last_audio
        st.rerun()
