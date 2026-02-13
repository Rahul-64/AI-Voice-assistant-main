# 🚀 Quick Deployment Guide (Windows)

Deploy your AI Voice Assistant to the web in minutes!

## Step 1: Test Locally (Windows)

```bash
# Open Command Prompt or PowerShell in project folder

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from .env.example)
copy .env.example .env

# Edit .env and add your API keys
notepad .env

# Run locally
streamlit run app.py
```

Visit: http://localhost:8501

---

## Step 2: Push to GitHub

```bash
# Install Git if not already: https://git-scm.com/download/win

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - AI Voice Assistant"

# Create a repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

---

## Step 3: Deploy (Choose One)

### Option A: Streamlit Cloud (Easiest - FREE)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Main file: `app.py`
6. Click "Advanced settings"
7. Add secrets:
   ```
   DEEPGRAM_API_KEY = "your_key"
   GROQ_API_KEY = "your_key"
   ```
8. Click "Deploy"
9. Done! Share your app URL

**Your app:** `https://your-app.streamlit.app`

---

### Option B: Render (FREE)

1. Go to https://render.com
2. Sign up/Login
3. Click "New +" → "Web Service"
4. Connect GitHub repo
5. Settings:
   - Name: ai-voice-assistant
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add Environment Variables:
   - `DEEPGRAM_API_KEY`
   - `GROQ_API_KEY`
7. Click "Create Web Service"
8. Wait ~5 minutes
9. Done!

**Your app:** `https://your-app.onrender.com`

---

## 📝 Before You Deploy

✅ Test locally first (`streamlit run app.py`)  
✅ Get API keys (Deepgram + Groq - both FREE)  
✅ Push to GitHub  
✅ Choose deployment platform  
✅ Add API keys as secrets  

---

## 🔑 Get API Keys (FREE)

### Deepgram
1. https://console.deepgram.com
2. Sign up → Create API Key
3. Copy it

### Groq
1. https://console.groq.com
2. Sign up → Generate API Key
3. Copy it

---

## 🎯 What You Get

- ✅ Live web app (public URL)
- ✅ AI chat interface
- ✅ Text-to-speech responses
- ✅ Mobile-friendly
- ✅ Free hosting!

---

## 🐛 Troubleshooting

**"Module not found"**
→ Redeploy or check requirements.txt

**"API Key Error"**
→ Add keys to platform secrets/environment variables

**"App won't start"**
→ Check deployment logs for errors

---

## 🎉 That's it!

Your AI Voice Assistant is now live and shareable!

For detailed instructions, see `DEPLOY_WEB.md`
