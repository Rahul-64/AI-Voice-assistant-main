# AI Voice Assistant - Web Version

A simple AI chatbot with text-to-speech, ready to deploy on Streamlit Cloud, Render, or other platforms.

## Quick Deploy

### 1. Get API Keys (FREE)
- **Deepgram**: https://console.deepgram.com
- **Groq**: https://console.groq.com

### 2. Deploy to Streamlit Cloud
1. Fork/Clone this repo
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Set main file: `app.py`
5. Add secrets:
   ```
   DEEPGRAM_API_KEY = "your_key"
   GROQ_API_KEY = "your_key"
   ```
6. Click Deploy!

## Features
- 🤖 AI-powered chat
- 🔊 Text-to-speech responses
- 💬 Clean web interface
- 📱 Mobile-friendly
- 🚀 Deploy in minutes

## Test Locally (Windows)

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Add your API keys to .env

# Run
streamlit run app.py
```

Visit: http://localhost:8501

## Deployment Guides
- **Quick Start (Windows)**: `QUICKSTART_WINDOWS.md`
- **Detailed Guide**: `DEPLOY_WEB.md`
- **Summary**: `DEPLOYMENT_SUMMARY.md`

## Tech Stack
- Streamlit (Web UI)
- Groq (AI - Llama 3.3 70B)
- Deepgram (Text-to-Speech)

## License
MIT - Free to use and modify

---

**Ready to deploy? See `QUICKSTART_WINDOWS.md`**
