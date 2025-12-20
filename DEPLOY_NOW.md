# R.A.S.T.E.R. - Deployment Guide

## 🚀 RECOMMENDED: Deploy to Render.com (Easiest)

**Why Render:**
- ✅ Free tier available
- ✅ Same platform as your Discord bot (easy integration later)
- ✅ Auto-deploy from GitHub
- ✅ Built-in SSL (HTTPS)
- ✅ No credit card required for free tier

---

## Step 1: Push to GitHub

### First Time Setup

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "R.A.S.T.E.R. website - ready to deploy"

# Create main branch
git branch -M main

# Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/raster-website.git

# Push to GitHub
git push -u origin main
```

### If You Don't Have a GitHub Repo Yet

1. Go to https://github.com/new
2. Repository name: `raster-website` (or your choice)
3. Description: "R.A.S.T.E.R. - An Analog Horror Story website"
4. **Leave it PUBLIC** (or private if you prefer)
5. **DO NOT** add README, .gitignore, or license (we already have them)
6. Click "Create repository"
7. Copy the commands shown and run them in your terminal

---

## Step 2: Deploy to Render.com

### A. Sign Up / Log In

1. Go to https://render.com
2. Click "Get Started"
3. Sign up with GitHub (easiest)

### B. Create New Web Service

1. Click "New +" in top right
2. Select "Web Service"
3. Click "Connect a repository"
4. Find and select your `raster-website` repository
5. Click "Connect"

### C. Configure Your Service

Render will auto-detect your `render.yaml` file, but verify these settings:

```
Name:           raster-website
Region:         Oregon (or closest to you)
Branch:         main
Build Command:  pip install -r requirements.txt
Start Command:  gunicorn app:app
```

### D. Environment Variables

**IMPORTANT:** Add these in the "Environment" section:

```
DISCORD_INVITE = https://discord.gg/Ywk54hKJ5H
SECRET_KEY = (Render will auto-generate this)
FLASK_ENV = production
```

### E. Choose Plan

- **Free:** $0/month (site sleeps after 15 min of inactivity)
- **Starter:** $7/month (always on, recommended)

### F. Deploy!

1. Click "Create Web Service"
2. Render will build and deploy your site
3. Wait 2-5 minutes for first deployment
4. You'll get a URL like: `https://raster-website.onrender.com`

---

## Step 3: Verify Deployment

Once deployed:

1. ✅ Visit your Render URL
2. ✅ Check Discord button works
3. ✅ Test on mobile
4. ✅ Verify all images load
5. ✅ Check redaction effects work

---

## Step 4: Add Custom Domain (Optional)

### If You Have a Domain:

1. Go to your service in Render
2. Click "Settings" tab
3. Scroll to "Custom Domains"
4. Click "Add Custom Domain"
5. Enter your domain (e.g., `raster.game` or `www.raster.game`)
6. Follow DNS configuration instructions

**DNS Setup:**
- Add CNAME record pointing to your Render URL
- Wait 10-60 minutes for DNS propagation

---

## Alternative: Deploy to Vercel (Also Easy)

### Quick Vercel Deploy

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy (from project folder)
vercel

# Follow prompts
# Set environment variables when asked:
vercel env add DISCORD_INVITE production
# Paste: https://discord.gg/Ywk54hKJ5H

# Deploy to production
vercel --prod
```

**Your site will be live at:** `https://your-project.vercel.app`

---

## Alternative: Deploy to Heroku

### Heroku Setup

```bash
# Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create raster-website

# Set environment variables
heroku config:set DISCORD_INVITE=https://discord.gg/Ywk54hKJ5H
heroku config:set FLASK_ENV=production

# Deploy
git push heroku main

# Open your site
heroku open
```

**Cost:** ~$7/month (no free tier as of Nov 2022)

---

## Troubleshooting Deployment

### "Build Failed"

**Check:**
- Python version in `runtime.txt` (should be `python-3.11.0`)
- All dependencies in `requirements.txt`
- No syntax errors (run `python app.py` locally first)

### "Application Error"

**Check:**
- Environment variables are set (especially `DISCORD_INVITE`)
- `Procfile` exists and is correct
- Check Render logs for specific error

### "Site is Slow"

**Free tier sleeps after inactivity**
- First load takes 30-60 seconds (waking up)
- Upgrade to paid tier for always-on

### "Discord Button Doesn't Work"

**Check:**
- Environment variable `DISCORD_INVITE` is set in Render dashboard
- Invite link is permanent (never expires)
- Test the invite link directly in browser

---

## Post-Deployment Checklist

After your site is live:

- [ ] Test Discord button on live site
- [ ] Test on mobile device
- [ ] Check all images load
- [ ] Verify redaction effects work
- [ ] Test from incognito/private window
- [ ] Share link with friends for testing
- [ ] Set up monitoring (optional): UptimeRobot.com
- [ ] Add analytics (optional): Google Analytics

---

## Updating Your Live Site

After making changes:

```bash
# Make your changes locally
# Test: python app.py

# Commit changes
git add .
git commit -m "Updated XYZ"

# Push to GitHub
git push

# Render auto-deploys! (if auto-deploy is enabled)
# Or click "Manual Deploy" in Render dashboard
```

---

## Cost Summary

### Render.com
- **Free tier:** $0/month (sleeps after inactivity)
- **Starter:** $7/month (always on, recommended)

### Vercel
- **Hobby:** Free (personal projects)
- **Pro:** $20/month (commercial use)

### Heroku
- **Basic:** ~$7/month (no free tier)

---

## Need Help?

**Render Documentation:** https://render.com/docs/web-services
**Vercel Documentation:** https://vercel.com/docs
**Heroku Documentation:** https://devcenter.heroku.com/

---

## 🎉 YOU'RE READY TO DEPLOY!

**Recommended path:**
1. Push to GitHub (5 minutes)
2. Deploy to Render.com (5 minutes)
3. Go live! (2-5 minutes build time)

**Total time: ~15 minutes from now to live site**

Let me know which platform you want to use and I can guide you through it!


