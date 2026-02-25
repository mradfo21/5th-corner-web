# 🚀 Render Deployment Guide

## Quick Deploy (Option 1: One-Click Deploy Button)

The easiest way to deploy is to click the **Deploy to Render** button:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/mradfo21/5th-corner-web)

**This button will:**
1. Take you to the Render Dashboard
2. Read the `render.yaml` blueprint from this repo
3. Create the service automatically
4. Start deployment immediately

**After clicking:**
1. Log in to Render (or sign up if you haven't)
2. Review the service configuration
3. Set the `DISCORD_INVITE` environment variable (required)
4. Click "Apply" to deploy
5. Wait 3-5 minutes for build to complete
6. You'll get a URL like: `https://5th-corner-website.onrender.com`

---

## Programmatic Deploy (Option 2: Python Script)

If you prefer to deploy via API:

### 1. Get Your Render API Key

1. Go to https://dashboard.render.com/u/settings?add-api-key
2. Click "Create API Key"
3. Give it a name: "5th Corner Website Deploy"
4. Copy the key (you'll only see it once!)

### 2. Add to Cursor Secrets

Add the key to your Cursor Cloud Agent secrets:
1. Go to [Cursor Dashboard](https://cursor.com/settings)
2. Navigate to: Cloud Agents > Secrets
3. Add new secret:
   - Name: `RENDER_API_KEY`
   - Value: (paste your API key)
   - Scope: This repository

### 3. Run Deployment Script

```bash
# If running locally, export the key:
export RENDER_API_KEY='your-key-here'

# Run deployment script:
python3 deploy_to_render.py
```

The script will:
- ✅ Check for existing 5th Corner services
- ✅ Create new service if needed
- ✅ Set all environment variables
- ✅ Trigger deployment
- ✅ Return your live URL

---

## Manual Deploy (Option 3: Render Dashboard)

### 1. Go to Render Dashboard
Visit: https://dashboard.render.com

### 2. Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub account (if not already connected)
3. Select repository: `mradfo21/5th-corner-web`
4. Click "Connect"

### 3. Configure Service
```
Name:           5th-corner-website
Region:         Oregon (or closest to you)
Branch:         main
Build Command:  pip install -r requirements.txt
Start Command:  gunicorn app:app
```

### 4. Set Environment Variables
**Required:**
- `DISCORD_INVITE` = `https://discord.gg/Ywk54hKJ5H` (or your invite)
- `FLASK_ENV` = `production`
- `PYTHON_VERSION` = `3.11.0`
- `GAME_API_URL` = `https://fiveth-corner-dev-1a00.onrender.com`

**Auto-generated:**
- `SECRET_KEY` = (let Render generate this)

### 5. Choose Plan
- **Free:** $0/month (sleeps after 15 min inactivity)
- **Starter:** $7/month (always-on, recommended)

### 6. Deploy
1. Click "Create Web Service"
2. Wait 3-5 minutes for build
3. Your site will be live!

---

## Deployment Status

Once deployed, you can:

1. **Check deployment logs**: https://dashboard.render.com
2. **Test health endpoint**: `https://your-service.onrender.com/health`
3. **View your site**:
   - Company page: `https://your-service.onrender.com/`
   - Game page: `https://your-service.onrender.com/raster`
   - Admin dashboard: `https://your-service.onrender.com/admin`

---

## Troubleshooting

### Build Failed
- Check Python version in `runtime.txt` (should be `python-3.11.0`)
- Verify all dependencies in `requirements.txt` are valid
- Check Render build logs for specific errors

### Service URL Not Loading
- Free tier services sleep after inactivity (first load takes 30-60s)
- Check service logs in Render dashboard
- Verify health endpoint returns `{"status": "ok"}`

### Discord Button Not Working
- Ensure `DISCORD_INVITE` environment variable is set
- Test the invite link directly in browser
- Check it's a permanent invite (never expires)

---

## Current Configuration

**Service Name:** `5th-corner-website` (from render.yaml)  
**Repository:** https://github.com/mradfo21/5th-corner-web  
**Branch:** main  
**Blueprint:** `render.yaml` (configured)  
**Python Version:** 3.11.0  
**Framework:** Flask + Gunicorn  
**Health Check:** `/health` endpoint

---

## Expected URL

After deployment, your site will be available at:
```
https://5th-corner-website.onrender.com
```

Or a custom URL if you configure one in Render settings.

---

## Next Steps After Deployment

1. ✅ Test all pages (/, /raster, /admin)
2. ✅ Verify Discord button works
3. ✅ Check mobile responsiveness
4. ✅ Set up custom domain (optional)
5. ✅ Enable monitoring/alerts in Render dashboard
6. ✅ Share the link!

---

**Ready to deploy?** Choose one of the three options above and your site will be live in minutes!
