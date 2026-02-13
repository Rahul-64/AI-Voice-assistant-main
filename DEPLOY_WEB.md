# AI Voice Assistant - Web Deployment Guide

Deploy your AI Voice Assistant to the cloud with these simple steps.

---

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended - FREE)

**Pros:** Free, easy setup, automatic updates from GitHub  
**Cons:** Public URL (anyone can access)

#### Steps:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Main file path: `app.py`
   - Click "Deploy"

3. **Add API Keys**
   - In Streamlit Cloud dashboard, click "⋮" → "Settings"
   - Go to "Secrets" section
   - Add:
     ```toml
     DEEPGRAM_API_KEY = "your_key_here"
     GROQ_API_KEY = "your_key_here"
     ```
   - Save and redeploy

4. **Done!** Your app will be live at `https://your-app-name.streamlit.app`

---

### Option 2: Render (FREE)

**Pros:** Free tier, easy deployment  
**Cons:** Spins down after 15 min of inactivity

#### Steps:

1. **Create `render.yaml`** (already included)

2. **Push to GitHub** (if not already done)

3. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Select "Python"
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - Click "Create Web Service"

4. **Add Environment Variables**
   - In dashboard, go to "Environment"
   - Add:
     - `DEEPGRAM_API_KEY`
     - `GROQ_API_KEY`
   - Save

5. **Done!** Your app will be live at `https://your-app-name.onrender.com`

---

### Option 3: Railway (FREE $5 credit/month)

**Pros:** Fast deployment, good free tier  
**Cons:** Credit runs out eventually

#### Steps:

1. **Push to GitHub**

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Select your repo
   - Railway auto-detects Streamlit

3. **Add Environment Variables**
   - In project settings, add:
     - `DEEPGRAM_API_KEY`
     - `GROQ_API_KEY`

4. **Generate Domain**
   - Go to "Settings" → "Generate Domain"

5. **Done!** Your app will be live at the generated URL

---

### Option 4: Hugging Face Spaces (FREE)

**Pros:** Free, ML-focused, good performance  
**Cons:** Requires Spaces setup

#### Steps:

1. **Create a Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Select "Streamlit" as SDK
   - Name your space

2. **Upload Files**
   - Upload `app.py`, `requirements.txt`, and `src/` folder
   - Or connect GitHub repo

3. **Add Secrets**
   - Go to Space Settings → "Repository secrets"
   - Add:
     - `DEEPGRAM_API_KEY`
     - `GROQ_API_KEY`

4. **Done!** Your app will be live at `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE`

---

## 📝 Pre-Deployment Checklist

- [ ] `.gitignore` includes `.env` and sensitive files
- [ ] `.env.example` shows required environment variables
- [ ] `requirements.txt` is up to date
- [ ] API keys are ready (Deepgram + Groq)
- [ ] Code is pushed to GitHub
- [ ] Test locally first: `streamlit run app.py`

---

## 🧪 Test Locally First

Before deploying, test your app locally:

```bash
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

Visit: `http://localhost:8501`

---

## 🔑 Getting API Keys (FREE)

### Deepgram (Speech)
1. Go to [console.deepgram.com](https://console.deepgram.com)
2. Sign up (free tier included)
3. Create new API key
4. Copy and save

### Groq (AI)
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free tier included)
3. Generate API key
4. Copy and save

---

## 🐛 Common Issues

### "API Key Not Found"
- Make sure secrets/environment variables are set correctly
- No extra spaces in keys
- Restart deployment after adding keys

### "Module Not Found"
- Check `requirements.txt` includes all dependencies
- Redeploy after updating requirements

### "App Not Loading"
- Check logs in deployment platform
- Verify Python version compatibility
- Ensure port settings are correct

---

## 📊 Platform Comparison

| Platform | Free Tier | Speed | Ease | Best For |
|----------|-----------|-------|------|----------|
| **Streamlit Cloud** | ✅ Unlimited | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Quick demos |
| **Render** | ✅ Yes | ⭐⭐⭐ | ⭐⭐⭐⭐ | Permanent apps |
| **Railway** | 💵 $5 credit | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Fast apps |
| **Hugging Face** | ✅ Unlimited | ⭐⭐⭐⭐ | ⭐⭐⭐ | ML projects |

---

## 🎯 Quick Deploy Commands

```bash
# 1. Test locally
streamlit run app.py

# 2. Git setup
git init
git add .
git commit -m "Deploy AI Voice Assistant"

# 3. Push to GitHub
git remote add origin YOUR_REPO_URL
git push -u origin main

# 4. Deploy on your chosen platform (see above)
```

---

## 🔒 Security Notes

- **Never commit `.env` files** (already in `.gitignore`)
- **Use platform secrets** for API keys
- **Rotate keys** if exposed
- **Monitor usage** to avoid unexpected charges

---

## 📞 Support

If you encounter issues:
1. Check platform-specific logs
2. Verify API keys are active
3. Test locally first
4. Check platform status pages

---

**Your app is ready to deploy! Choose your platform and follow the steps above.**

Last Updated: February 2025
