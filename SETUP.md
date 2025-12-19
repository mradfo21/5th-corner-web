# SOMEWHERE Website - Setup Guide

Quick start guide to get the website running locally and deployed.

---

## ⚡ Quick Setup (5 minutes)

### 1. Install Dependencies

```bash
# Clone or navigate to project
cd somewhere-website

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 2. Configure Environment

Create `.env` file in root directory:

```bash
DISCORD_INVITE=https://discord.gg/YOUR_INVITE_CODE
SECRET_KEY=change-this-to-something-random
FLASK_ENV=development
```

To generate a secure secret key:

```python
python -c "import secrets; print(secrets.token_hex(32))"
```

### 3. Add Images (Optional but Recommended)

Copy 4 gameplay images from your bot:

```bash
# Windows
copy "C:\path\to\bot\cache\frame_001.png" "static\images\examples\example1.png"

# macOS/Linux
cp /path/to/bot/cache/frame_001.png static/images/examples/example1.png
```

See `static/images/PLACEHOLDER_IMAGES.md` for details.

### 4. Run Development Server

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## 🚀 Deployment Setup

### Option A: Render.com (Recommended, Easiest)

**Why Render?**
- ✅ Free tier available
- ✅ Auto-deploy from GitHub
- ✅ Built-in SSL
- ✅ Same platform as Discord bot

**Steps:**

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/somewhere-website.git
git push -u origin main
```

2. **Deploy on Render**
   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect GitHub repository
   - Render auto-detects `render.yaml`
   - Click "Create Web Service"

3. **Set Environment Variables**
   - Go to Environment tab
   - Add `DISCORD_INVITE` with your Discord link
   - `SECRET_KEY` is auto-generated

4. **Done!**
   - Your site will be live at `https://somewhere-website.onrender.com`
   - Add custom domain if desired

**Cost**: Free tier with limitations (site sleeps after inactivity), $7/month for always-on

### Option B: Vercel (Fast & Free)

**Steps:**

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Deploy**
```bash
vercel
```

3. **Set Environment Variables**
```bash
vercel env add DISCORD_INVITE
vercel env add SECRET_KEY
```

4. **Done!**
   - Site live at `https://your-project.vercel.app`

**Cost**: Free for personal projects

### Option C: Heroku

**Steps:**

1. **Install Heroku CLI**
   - macOS: `brew install heroku/brew/heroku`
   - Windows: Download from heroku.com

2. **Deploy**
```bash
heroku login
heroku create somewhere-website
git push heroku main
```

3. **Set Environment Variables**
```bash
heroku config:set DISCORD_INVITE=https://discord.gg/YOUR_INVITE
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
```

4. **Open**
```bash
heroku open
```

**Cost**: ~$7/month (no free tier as of Nov 2022)

---

## 🎨 Customization

### Change Discord Invite Link

**Option 1: Environment Variable (Recommended)**
```bash
# Update .env file
DISCORD_INVITE=https://discord.gg/NEW_INVITE_CODE
```

**Option 2: Direct in Code**
Edit `app.py`:
```python
DISCORD_INVITE = 'https://discord.gg/YOUR_INVITE_CODE'
```

### Change Colors

Edit `static/css/style.css`:

```css
:root {
    --color-vhs-red: #FF0033;      /* Primary accent color */
    --color-phosphor-green: #00FF41; /* Secondary accent */
    --color-near-black: #0A0A0A;   /* Background */
}
```

### Change Text Content

Edit `templates/index.html`:

```html
<h1 class="hero-title">SOMEWHERE</h1>
<p class="hero-tagline">Your custom tagline here</p>
```

### Disable VHS Scanlines

Edit `static/css/style.css`:

```css
:root {
    --scanline-opacity: 0;  /* Change from 0.05 to 0 */
}
```

### Add Custom Fonts

1. Download font files to `static/fonts/`
2. Edit `templates/base.html`:
```html
<link href="path/to/your/font.css" rel="stylesheet">
```
3. Edit `static/css/style.css`:
```css
:root {
    --font-mono: 'YourFont', monospace;
}
```

---

## ✅ Pre-Deployment Checklist

Before going live:

- [ ] Replace example images with real gameplay screenshots
- [ ] Update `DISCORD_INVITE` with permanent invite link
- [ ] Generate secure `SECRET_KEY`
- [ ] Test on mobile device
- [ ] Verify Discord invite link works
- [ ] Check all links open in new tabs
- [ ] Test image loading
- [ ] Verify OG image for social sharing
- [ ] Add favicon and apple-touch-icon
- [ ] Test page load speed (should be < 2s)
- [ ] Check accessibility (keyboard navigation)
- [ ] Proofread all copy

---

## 🧪 Testing

### Local Testing

```bash
# Run development server
python app.py

# Open in browser
# Visit http://localhost:5000
```

### Test on Mobile

**Option 1: ngrok (Easiest)**
```bash
# Install ngrok from ngrok.com
ngrok http 5000

# Use the https URL on your phone
```

**Option 2: Local Network**
```bash
# Find your local IP
# Windows: ipconfig
# macOS/Linux: ifconfig

# Run Flask with host binding
python app.py

# Visit http://YOUR_LOCAL_IP:5000 on phone
```

### Browser Testing

Test on:
- Chrome (desktop & mobile)
- Firefox
- Safari (macOS & iOS)
- Edge

Check:
- ✅ All sections visible
- ✅ Buttons clickable
- ✅ Images load
- ✅ No console errors
- ✅ Discord link works
- ✅ Smooth scrolling
- ✅ VHS effects render

---

## 🐛 Common Issues

### "No module named 'flask'"
**Fix**: Activate virtual environment first
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Then install
pip install -r requirements.txt
```

### Images not showing
**Fix**: Check file paths and names match exactly
```bash
# Verify images exist
ls static/images/examples/

# File names must match templates/index.html
```

### Port 5000 already in use
**Fix**: Use different port
```bash
# In app.py, change:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Styles not updating
**Fix**: Hard refresh browser
- Chrome/Firefox: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Or disable cache in DevTools (F12 → Network tab → "Disable cache")

### Discord invite expired
**Fix**: Create permanent invite
- Discord → Server Settings → Invites
- Create new invite
- Set "Expire after" to "Never"
- Update `DISCORD_INVITE` environment variable

---

## 📊 Monitoring (Optional)

### Add Health Check Monitoring

Services like **UptimeRobot** or **Better Uptime** can monitor your `/health` endpoint:

1. Sign up at uptimerobot.com (free)
2. Add monitor: `https://your-site.com/health`
3. Get alerts if site goes down

### Add Analytics

1. **Google Analytics**
   - Get tracking ID from analytics.google.com
   - Add to `templates/base.html` before `</head>`

2. **Plausible** (privacy-friendly alternative)
   - Sign up at plausible.io
   - Add one-line script to template

---

## 🔐 Security

### Before Going Live

1. **Change SECRET_KEY**
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

2. **Use HTTPS** (automatic on Render/Vercel/Heroku)

3. **Don't commit .env** (already in .gitignore)

4. **Keep dependencies updated**
   ```bash
   pip list --outdated
   pip install --upgrade flask gunicorn
   ```

---

## 📞 Need Help?

- **Documentation**: See README.md
- **Issues**: GitHub Issues
- **Discord**: Join your SOMEWHERE server
- **Deployment**: Check platform docs (Render/Vercel/Heroku)

---

**You're ready to go!** 🎬

Start with local development, test thoroughly, then deploy to Render/Vercel.

*"1993. You are recording. The world does not care if you survive."*

