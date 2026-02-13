# 🎤 AI Voice Assistant

An advanced AI voice assistant with both desktop and web interfaces, featuring real-time speech-to-text, text-to-speech, and intelligent agent capabilities.

![Python](https://img.shields.io/badge/python-3.8+-blue)
![LiteLLM](https://img.shields.io/badge/LiteLLM-Enabled-green)
![Deepgram](https://img.shields.io/badge/Deepgram-Speech-orange)

---

## ✨ Features

### Core Capabilities
- 🎙️ **Voice Interaction** - Real-time speech-to-text using Deepgram
- 🔊 **Natural Voice Responses** - High-quality text-to-speech with Deepgram TTS
- 🤖 **Advanced AI** - Powered by Groq Llama 3.3 70B (or any LiteLLM-compatible model)
- ⏸️ **Speech Interruption** - Press SPACE to interrupt AI mid-sentence
- 🛠️ **Agent System** - Modular tool-based architecture





---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Microphone (for voice input)
- Speakers/Headphones (for voice output)

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Voice-assistant.git
cd AI-Voice-assistant-main
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get API Keys (FREE)

**Required:**
- **Deepgram API Key**: https://console.deepgram.com (for speech-to-text & text-to-speech)
- **Groq API Key**: https://console.groq.com (for AI language model)



### 4. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your API keys
DEEPGRAM_API_KEY=your_deepgram_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Assistant

**Option A: Desktop Voice Assistant**
```bash
python main.py
```

---

## 📖 Usage Guide

### Desktop Voice Assistant

1. **Start the assistant**: `python main.py`
2. **Speak clearly** when prompted
3. **Wait for AI response** - The AI will speak back
4. **Press SPACE** anytime to interrupt the AI
5. **Say "goodbye"** to exit

#### Keyboard Controls

| Key | Action |
|-----|--------|
| **SPACE** | Interrupt AI speech immediately |
| **Ctrl+C** | Exit the program |

### Web Interface

1. **Start the web app**: `streamlit run app.py`
2. **Type your message** in the input field
3. **Click Send** or press Enter
4. **Listen to AI response** - Audio plays automatically
5. **Press SPACE** to interrupt (in supported browsers)

---


### Customization

**Change AI Personality:**

Edit `main.py` around line 11:

```python
simple_prompt = """You are a helpful and friendly AI assistant..."""
```

**Change Colors (Web UI):**

Edit the CSS section in `app.py`:

```css
.stApp {
    background: linear-gradient(135deg, 
        #YOUR_COLOR1 0%, 
        #YOUR_COLOR2 50%, 
        #YOUR_COLOR3 100%) !important;
}
```

---

## 🔧 Advanced Configuration

### Using Different AI Models

The assistant supports any LiteLLM-compatible model. Edit `main.py`:

```python
# Examples:
model = "groq/llama-3.3-70b-versatile"  # Default
model = "openai/gpt-4"                   # OpenAI
model = "anthropic/claude-3-opus"        # Anthropic
model = "gemini/gemini-pro"              # Google
```



---

## 📂 Project Structure

```
AI-Voice-assistant-main/
├── main.py                          # Desktop voice assistant entry point
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── .env                            # Your API keys (create this)
├── .streamlit/
│   ├── config.toml                 # Streamlit theme configuration
│   └── secrets.toml                # Streamlit secrets (for deployment)
├── src/
│   ├── agents/
│   │   └── agent.py                # Core AI agent logic
│   ├── speech_processing/
│   │   ├── speech_to_text.py      # Deepgram STT
│   │   ├── text_to_speech.py      # Deepgram TTS with interruption
│   │   └── conversation_manager.py # Conversation flow handler
│   ├── prompts/
│   │   └── prompts.py             # System prompts
│   └── utils.py                   # Utility functions
├── scripts/
│   ├── create_index.py            # Knowledge base indexing
│   └── fetch_index.py             # Knowledge base retrieval
├── INTERRUPTION_FEATURE.md         # Detailed interruption feature docs
├── README_WEB.md                   # Web deployment guide
└── README.md                       # This file
```

---

## 🌐 Deploy to Cloud

### Streamlit Cloud (Recommended for Web UI)

1. **Fork this repository** on GitHub
2. **Go to** https://share.streamlit.io
3. **Sign in** with GitHub
4. **Click "New app"**
5. **Select your repository**
6. **Set main file**: `app.py`
7. **Add secrets** in Streamlit dashboard:
   ```toml
   DEEPGRAM_API_KEY = "your_key_here"
   GROQ_API_KEY = "your_key_here"
   ```
8. **Click Deploy!**

Your app will be live at: `https://your-app-name.streamlit.app`

### Other Platforms
- **Render**: See `README_WEB.md`
- **Railway**: Compatible with Streamlit
- **Heroku**: Requires Procfile (add: `web: streamlit run app.py`)

---

## 🐛 Troubleshooting

### Desktop Assistant

**Microphone not detected?**
- Check microphone permissions in system settings
- Ensure microphone is set as default recording device
- Test with: `python -c "import sounddevice; print(sounddevice.query_devices())"`

**SPACE key not interrupting?**
- Ensure terminal window has focus
- Check for message: `[Keyboard listener active - SPACE to interrupt]`
- Verify `pynput` is installed: `pip install pynput`

**Audio playback issues?**
- Install audio dependencies: `pip install librosa soundfile`
- Check speaker/headphone connection
- Verify system audio is not muted

**API errors?**
- Verify API keys are correct in `.env` file
- Check for extra spaces or quotes in API keys
- Ensure API keys are active (check provider dashboard)

### Web Interface

**Gradient not showing?**
- Clear browser cache and hard refresh (Ctrl+F5)
- Try a different browser (Chrome recommended)

**Audio not playing?**
- Check browser allows audio autoplay
- Ensure speakers/headphones are connected
- Check browser console for errors (F12)

**Deployment fails?**
- Verify `requirements.txt` includes all dependencies
- Check Python version compatibility (3.8+)
- Ensure API keys are set in deployment platform secrets

---

## 🎯 Key Features Explained

### Speech Interruption
Press **SPACE** at any time while the AI is speaking to immediately stop playback. This allows natural, responsive conversations where you can interrupt and redirect the AI without waiting for it to finish.

**Technical Details:**
- Interruption latency: <100ms
- Works during audio generation and playback
- Clean recovery with no audio artifacts
- See `INTERRUPTION_FEATURE.md` for more details

### Agent System
The assistant uses a modular agent architecture where tools can be dynamically added:
- Tools are defined as Python classes inheriting from `BaseTool`
- Each tool has an OpenAI-compatible schema
- The agent automatically handles tool selection and execution
- See `src/tools/base_tool.py` for creating custom tools

### LiteLLM Integration
Supports 100+ AI models through LiteLLM:
- Unified API for all providers
- Automatic fallbacks and retries
- Cost tracking and caching
- Easy model switching

---

## 🧪 Testing

**Test interruption feature:**
```bash
python test_interruption.py  # If available
```

**Test individual components:**
```python
# Test Speech-to-Text
from src.speech_processing.speech_to_text import get_transcript
import asyncio
asyncio.run(get_transcript(lambda text: print(f"You said: {text}")))

# Test Text-to-Speech
from src.speech_processing.text_to_speech import TTS
tts = TTS()
tts.speak("Hello! I am your AI assistant.")
```

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Open a Pull Request

---

## 📝 License

MIT License - Free to use and modify

---

## 🙏 Credits

**Built with:**
- [Deepgram](https://deepgram.com) - Speech-to-Text & Text-to-Speech
- [Groq](https://groq.com) - Ultra-fast AI inference
- [LiteLLM](https://litellm.ai) - Unified LLM API
- [Streamlit](https://streamlit.io) - Web interface framework
- [Pynput](https://pynput.readthedocs.io) - Keyboard event handling

---

