# 🎙️ AI Voice Assistant

A real-time voice-powered AI assistant that listens to your voice, processes requests using LLM, and responds with natural speech. Features instant keyboard interruption for natural conversation flow.

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

**Transform your digital interactions with intelligent voice conversations! 🎙️🤖**

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo Flow](#-demo-flow)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Interruption Feature](#-interruption-feature)
- [Troubleshooting](#-troubleshooting)
- [Performance](#-performance)
- [File Structure](#-file-structure)
- [Recent Updates](#-recent-updates)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Capabilities
- 🎤 **Real-time Speech-to-Text** - Powered by Deepgram's Nova-2 model
- 🤖 **AI Conversation** - Uses Groq's Llama 3.3 70B model
- 🔊 **Text-to-Speech** - Natural voice responses via Deepgram Aura
- ⚡ **Fast Response Time** - Processes queries in 2-5 seconds
- ⌨️ **Keyboard Interruption** - Press SPACE to interrupt AI mid-speech
- 🔄 **Continuous Conversation** - Seamless back-and-forth dialogue

### Technical Features
- ✅ Python 3.12 compatible
- ✅ Cross-platform (Windows, Mac, Linux)
- ✅ Async/await architecture for responsiveness
- ✅ Proper websocket connection management
- ✅ Real-time audio streaming
- ✅ Clean error handling and recovery

---

## 🎬 Demo Flow

```
┌─────────────────────────────────────────────────────────┐
│  AI VOICE ASSISTANT - Simple Chat Mode                 │
└─────────────────────────────────────────────────────────┘

[Microphone Active - Start Speaking]
🎤 You: "Hello, how are you?"

[Transcription Complete - Processing...]
Human: Hello, how are you?

[AI is thinking...]
AI: I'm doing great, thanks for asking!
[Processing took 0.91 seconds]

[Speaking response...]
🔊 (AI speaks the response)

[Press SPACE to interrupt anytime]

=== Ready to listen ===
🎤 (Waiting for your next question...)
```

---

## 📦 Requirements

### System Requirements
- Python 3.12 or higher
- Microphone and speakers/headphones
- Internet connection (for API calls)
- Windows/Mac/Linux OS

### API Keys Required
- **Deepgram API Key** - For speech-to-text and text-to-speech ([Get it here](https://deepgram.com))
- **Groq API Key** - For LLM processing ([Get it here](https://groq.com))

### Python Libraries
All dependencies are listed in `requirements.txt`:
```
litellm
deepgram-sdk
pygame
pyaudio
python-dotenv
pydantic
colorama
pynput
```

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Voice-assistant.git
cd AI-Voice-assistant
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Create `.env` File

Create a `.env` file in the project root:

```env
DEEPGRAM_API_KEY=your_deepgram_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### Get API Keys

1. **Deepgram API Key:**
   - Go to [console.deepgram.com](https://console.deepgram.com)
   - Sign up / Log in
   - Create a new API key
   - Copy and paste into `.env`

2. **Groq API Key:**
   - Go to [console.groq.com](https://console.groq.com)
   - Sign up / Log in
   - Generate API key
   - Copy and paste into `.env`

---

## 🎮 Usage

### Start the Assistant

```bash
python main.py
```

### Instructions Display
```
============================================================
AI VOICE ASSISTANT - Simple Chat Mode
============================================================
Instructions:
  1. Speak clearly when prompted
  2. Pause when done speaking (system auto-detects)
  3. Wait for AI response
  4. Press SPACE to interrupt AI while speaking
  5. Say 'goodbye' to exit
============================================================
```

### Basic Conversation Example

```
=== Ready to listen ===
[Microphone Active - Start Speaking]

You: "What's 2 plus 2?"
AI: "The answer is 4."

You: "Tell me a joke"
AI: "Why did the chicken cross the road? To get to the other side!"

You: "Goodbye"
[Goodbye! Shutting down...]
```

### Interruption Example

```
You: "Tell me a very long story about..."
AI: "Once upon a time, in a faraway land..."

[You press SPACE]
[!] SPACE pressed - Interrupting AI...
[TTS] Playback interrupted by user!

You: "Actually, what's the weather?"
AI: "I don't have access to real-time weather data..."
```

---

## 🏗️ Architecture

### System Flow

```
┌─────────────┐
│  Microphone │
└──────┬──────┘
       │ Audio Stream
       ▼
┌──────────────────┐
│ Deepgram STT     │ ← Speech-to-Text
│ (Nova-2 Model)   │
└──────┬───────────┘
       │ Transcribed Text
       ▼
┌──────────────────┐
│ Groq LLM         │ ← AI Processing
│ (Llama 3.3 70B)  │
└──────┬───────────┘
       │ AI Response Text
       ▼
┌──────────────────┐
│ Deepgram TTS     │ ← Text-to-Speech
│ (Aura Model)     │
└──────┬───────────┘
       │ Audio Output
       ▼
┌─────────────┐
│  Speakers   │
└─────────────┘
```

### Key Components

1. **speech_to_text.py**
   - Manages microphone input
   - Streams audio to Deepgram
   - Handles websocket connection
   - Detects speech completion
   - Sends Finalize signal for clean shutdown

2. **agent.py**
   - Manages conversation context
   - Calls LLM API (Groq)
   - Handles message history
   - Formats responses

3. **text_to_speech.py**
   - Generates speech from text
   - Plays audio using pygame
   - Supports interruption via threading flag
   - Checks for SPACE key every 100ms

4. **conversation_manager.py**
   - Orchestrates the conversation loop
   - Manages keyboard listener
   - Handles interruption logic
   - Coordinates STT → LLM → TTS flow

---

## ⌨️ Interruption Feature

### How It Works

The assistant can be interrupted **instantly** while speaking by pressing the **SPACE** key.

### Implementation Details

- **Keyboard Listener:** Background thread monitors SPACE key
- **Interruption Flag:** `threading.Event()` signals TTS to stop
- **Check Frequency:** Every 100ms during audio playback
- **Latency:** < 100 milliseconds (instant response)

### Use Cases

1. **AI is wrong:** Stop mid-response to correct
2. **Change topic:** Interrupt to ask something else
3. **Response too long:** Skip to ask follow-up
4. **Misunderstood query:** Stop and rephrase

### Testing Interruption

```bash
python test_interruption.py
```

This runs a dedicated test where you can practice interrupting a long speech.

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **Microphone Not Working**
```
Error: Could not open socket
```
**Solution:**
- Check microphone permissions
- Verify microphone is connected
- Test with: `python -c "import pyaudio; p=pyaudio.PyAudio(); print('OK')"`

#### 2. **API Key Errors**
```
Error: 403 Forbidden / Unauthorized
```
**Solution:**
- Check `.env` file exists
- Verify API keys are correct
- Ensure no extra spaces in `.env`
- Restart terminal after adding keys

#### 3. **Audio Not Playing**
```
[TTS] Audio generated but no sound
```
**Solution:**
- Check speaker volume
- Verify audio output device
- Test with: `python test_tts.py`
- Check pygame initialization messages

#### 4. **Slow Response Time**
```
[Processing took 30+ seconds]
```
**Solution:**
- Check internet connection
- Verify Groq API is responding
- Run speed test: `python test_speed.py`
- Expected: 0.9-3 seconds

#### 5. **Interruption Not Working**
```
SPACE key doesn't stop AI
```
**Solution:**
- Ensure terminal window has focus
- Check for: `[Keyboard listener active]` message
- Verify `pynput` is installed
- Try re-running: `pip install pynput`

### Debug Mode

For verbose output, check console messages:
- `[STT]` - Speech-to-text events
- `[TTS]` - Text-to-speech events  
- `[AI is thinking...]` - LLM processing
- `[Processing took X.XX seconds]` - Performance metrics

---

## 📊 Performance

### Speed Benchmarks

| Operation | Time | Notes |
|-----------|------|-------|
| Speech Recognition | 0.5-2s | After you stop speaking |
| LLM Processing | 0.9-3s | Depends on query complexity |
| Speech Generation | 1-2s | Depends on response length |
| **Total Response Time** | **2-5s** | Complete cycle |

### Optimization Features

- ✅ **WebSocket Finalize:** Eliminates 10-30s timeout
- ✅ **No Tools:** Removed Calendar/Email/Search for speed
- ✅ **Async Architecture:** Non-blocking operations
- ✅ **Efficient Audio Streaming:** Real-time processing

### Resource Usage

- **RAM:** ~200-300 MB
- **CPU:** 5-15% during listening
- **Network:** Continuous during STT, bursts for LLM/TTS
- **Disk:** Minimal (temporary audio files)

---

## 📁 File Structure

```
AI-Voice-assistant-main/
├── main.py                          # Entry point
├── requirements.txt                 # Dependencies
├── .env                            # API keys (create this)
├── README.md                       # This file
│
├── src/
│   ├── agents/
│   │   └── agent.py                # LLM agent logic
│   │
│   ├── speech_processing/
│   │   ├── speech_to_text.py       # STT with Deepgram
│   │   ├── text_to_speech.py       # TTS with Deepgram
│   │   └── conversation_manager.py # Main conversation loop
│   │
│   └── prompts/
│       └── prompts.py              # System prompts
│
├── tests/
│   ├── test_simple.py              # Component tests
│   ├── test_agent.py               # Agent tests
│   ├── test_speed.py               # Performance tests
│   ├── test_tts.py                 # TTS tests
│   └── test_interruption.py        # Interruption tests
│
└── docs/
    ├── FIX_SUMMARY.md              # Initial fixes
    ├── FINAL_FIX.md                # WebSocket optimization
    ├── INTERRUPTION_FEATURE.md     # Interruption details
    └── HOW_IT_WORKS.md             # User guide
```

---

## 🆕 Recent Updates

### Version 2.0 - Current (2025)

#### Major Fixes
- ✅ **Python 3.12 Compatibility** - Updated all deprecated packages
- ✅ **Deepgram SDK v5.3.2** - Migrated from v3 to v5 API
- ✅ **WebSocket Optimization** - Fixed keepalive timeout (10-30s → instant)
- ✅ **TTS Audio Fix** - Corrected generator handling
- ✅ **Keyboard Interruption** - Added SPACE key interrupt feature

#### Performance Improvements
- ⚡ Response time: 60+ seconds → 2-5 seconds
- ⚡ Added proper Finalize signal to Deepgram
- ⚡ Removed tool integrations for speed
- ⚡ Optimized audio streaming

#### API Changes
```python
# Old (v3)
from deepgram import DeepgramClientOptions, LiveOptions, Microphone
config = DeepgramClientOptions(options={"keepalive": "true"})

# New (v5.3.2)
from deepgram import DeepgramClient
from deepgram.extensions.types.sockets import ListenV1MediaMessage
with deepgram.listen.v1.connect(...) as connection:
    connection.send_media(ListenV1MediaMessage(audio_data))
```

---

## 🔮 Future Enhancements

### Planned Features

#### Voice Interruption (Option 2)
- Interrupt by speaking (hands-free)
- Voice Activity Detection (VAD)
- Requires headphones for echo cancellation
- Natural interruption without keyboard

#### Keyword Detection (Option 3)
- Say "stop", "wait", "hold on" to interrupt
- Intentional interruption only
- Real-time keyword spotting
- No accidental interruptions

#### Tool Integration (Optional)
- Google Calendar integration
- Email sending capability
- Web search functionality
- Contact management
- *Currently disabled for speed*

#### Multi-Language Support
- Spanish, French, German, etc.
- Language auto-detection
- Multi-lingual responses

#### Conversation Memory
- Long-term context retention
- Reference previous conversations
- User preferences storage

---

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly: `python test_simple.py`
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Create Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Include error handling
- Add tests for new features

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- **Deepgram** - Speech-to-Text and Text-to-Speech APIs
- **Groq** - Lightning-fast LLM inference
- **LiteLLM** - Unified LLM interface
- **PyGame** - Audio playback
- **PyAudio** - Microphone input
- **Pynput** - Keyboard detection

---

## 📞 Support

### Getting Help

1. Check [Troubleshooting](#-troubleshooting) section
2. Review documentation in `docs/` folder
3. Run diagnostic tests: `python test_simple.py`
4. Check API status:
   - [Deepgram Status](https://status.deepgram.com)
   - [Groq Status](https://status.groq.com)

### Useful Commands

```bash
# Test all components
python test_simple.py

# Test agent speed
python test_speed.py

# Test TTS only
python test_tts.py

# Test interruption
python test_interruption.py

# Run main assistant
python main.py
```

---

## 🎯 Quick Start Summary

```bash
# 1. Setup
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 2. Configure
# Create .env with your API keys

# 3. Run
python main.py

# 4. Use
# Speak → AI responds → Press SPACE to interrupt
# Say "goodbye" to exit
```

---

**Built with ❤️ for natural voice interactions**

*Last Updated: February 2025 | Version 2.0*
