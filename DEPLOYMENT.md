# AI Voice Assistant

A simple, real-time voice AI assistant that listens, processes, and responds with natural speech.

## Quick Start

### 1. Prerequisites
- Python 3.12 or higher
- Microphone and speakers
- Internet connection

### 2. Installation

```bash
# Clone or download this repository
git clone <your-repo-url>
cd AI-Voice-assistant-main

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the project root and add your API keys:

```env
DEEPGRAM_API_KEY=your_deepgram_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**Get your FREE API keys:**
- Deepgram (Speech): https://console.deepgram.com
- Groq (AI): https://console.groq.com

### 4. Run

```bash
python main.py
```

## How to Use

1. Start speaking when prompted
2. System will auto-detect when you're done
3. AI processes and responds
4. Press **SPACE** to interrupt AI mid-speech
5. Say "goodbye" to exit

## Features

- Real-time speech recognition (Deepgram Nova-2)
- Fast AI responses (Groq Llama 3.3 70B)
- Natural voice output (Deepgram Aura)
- Keyboard interruption support
- 2-5 second response time

## Customization

Edit the `simple_prompt` in `main.py` to change the AI's personality and behavior.

## Troubleshooting

**Microphone not working?**
- Check microphone permissions
- Verify microphone is connected

**API errors?**
- Check `.env` file has correct keys
- Verify no extra spaces in API keys

**No audio output?**
- Check speaker volume
- Verify audio output device

## System Requirements

- RAM: 200-300 MB
- CPU: 5-15% during listening
- Network: Required for API calls

## License

MIT License - Free to use and modify

## Support

Check the full documentation in README.md for detailed troubleshooting and advanced features.
