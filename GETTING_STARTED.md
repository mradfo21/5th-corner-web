# SOMEWHERE Website - Getting Started

## 🎬 Quick Start (3 Steps)

### Step 1: Configure Discord Invite

Open `.env` file and replace `YOUR_INVITE_CODE` with your actual Discord invite:

```bash
DISCORD_INVITE=https://discord.gg/YOUR_ACTUAL_INVITE_HERE
```

**To get a permanent Discord invite:**
1. Open your SOMEWHERE Discord server
2. Right-click on a channel → "Edit Channel"
3. Go to "Invites" → "Create Invite"
4. Set "Expire after" to **Never**
5. Copy the invite link

### Step 2: Install Dependencies (If Needed)

```bash
# Only if Flask is not installed
pip install Flask gunicorn python-dotenv
```

### Step 3: Run the Development Server

```bash
python app.py
```

Visit: **http://localhost:5000**

---

## ✅ What You Get

Your website is **100% ready to deploy** with:

- ✅ VHS analog horror aesthetic
- ✅ Mobile-responsive design
- ✅ Conversion-focused layout
- ✅ Placeholder images (replace with real ones)
- ✅ SEO meta tags
- ✅ Production-ready code

---

## 🖼️ Replace Placeholder Images

The website currently has placeholder images. Replace them with real gameplay screenshots:

### Quick Replace

```bash
# Copy 4 frames from your bot's cache
copy "C:\path\to\bot\cache\frame_001.png" "static\images\examples\example1.png"
copy "C:\path\to\bot\cache\frame_045.png" "static\images\examples\example2.png"
copy "C:\path\to\bot\cache\frame_089.png" "static\images\examples\example3.png"
copy "C:\path\to\bot\cache\frame_120.png" "static\images\examples\example4.png"
```

### Image Requirements

- **Format**: PNG or JPEG
- **Size**: 800x600px (recommended)
- **Content**: VHS-style gameplay frames
- **Captions**: Edit in `templates/index.html`

---

## 🚀 Deploy to Production

### Option 1: Render.com (Easiest)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: SOMEWHERE website"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/somewhere-website.git
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render detects `render.yaml` automatically
   - Click "Create Web Service"

3. **Set Discord Invite**
   - Go to Environment tab
   - Add `DISCORD_INVITE` = your actual Discord link
   - Click "Save Changes"

4. **Done!**
   - Site goes live at `https://somewhere-website.onrender.com`
   - Automatic SSL certificate
   - Auto-deploys on git push

**Cost:** Free tier available (sleeps after inactivity) or $7/month for always-on

### Option 2: Vercel (Fast & Free)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Set environment variables
vercel env add DISCORD_INVITE
# Paste your Discord invite when prompted
```

**Cost:** Free for personal projects

---

## 🎨 Customize

### Change Colors

Edit `static/css/style.css`:

```css
:root {
    --color-vhs-red: #FF0033;      /* Change to your color */
    --color-phosphor-green: #00FF41;
    --color-near-black: #0A0A0A;
}
```

### Change Text

Edit `templates/index.html`:

```html
<h1 class="hero-title">SOMEWHERE</h1>
<p class="hero-tagline">Your custom tagline here</p>
```

### Disable Scanlines

Edit `static/css/style.css`:

```css
:root {
    --scanline-opacity: 0;  /* Change from 0.05 to 0 */
}
```

---

## 📱 Test on Mobile

### Method 1: ngrok (Easiest)

```bash
# Download ngrok from ngrok.com
ngrok http 5000

# Use the https URL on your phone
```

### Method 2: Local Network

```bash
# Find your local IP
ipconfig  # Windows
ifconfig  # macOS/Linux

# Visit http://YOUR_LOCAL_IP:5000 on your phone
```

---

## ✅ Pre-Launch Checklist

Before deploying:

- [ ] Discord invite link set (permanent, never expires)
- [ ] Real gameplay images added (or placeholders are OK)
- [ ] Tested on Chrome, Firefox, Safari
- [ ] Tested on mobile device
- [ ] Discord invite button works
- [ ] All images load correctly
- [ ] No console errors in browser DevTools
- [ ] Page loads in < 3 seconds

---

## 🆘 Troubleshooting

### "Module 'flask' not found"

```bash
pip install Flask
```

### "Port 5000 already in use"

Edit `app.py`, change:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Images not loading

- Check file names match exactly (case-sensitive on Linux/Mac)
- Verify files exist in `static/images/examples/`
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

### Discord invite expired

- Create a new **permanent** invite (set "Expire after" to "Never")
- Update `.env` file with new link
- Restart Flask app

---

## 📚 Documentation

- **README.md** - Full documentation
- **SETUP.md** - Detailed setup guide
- **PROJECT_SUMMARY.md** - Technical overview
- **PLACEHOLDER_IMAGES.md** - Image guide

---

## 🎯 What's Next?

### Immediate
1. ✅ Set Discord invite
2. ✅ Test locally
3. ✅ Add real images
4. ✅ Deploy to Render/Vercel

### Future (Phase 2)
- Live stats from Discord bot
- Real-time gallery of generated images
- API integration

### Future (Phase 3)
- Play from browser (web UI)
- User accounts
- Tape library
- Community features

---

## 💡 Tips

- **Keep it simple**: Phase 1 is conversion-focused, not feature-heavy
- **Real images matter**: Placeholders work, but real gameplay is better
- **Mobile first**: Most visitors will be on phones
- **Fast loading**: Keep images optimized (< 500KB each)
- **Permanent invite**: Make sure Discord link never expires

---

## 🔗 Quick Links

- **Local site**: http://localhost:5000
- **Render docs**: https://render.com/docs
- **Vercel docs**: https://vercel.com/docs
- **Flask docs**: https://flask.palletsprojects.com

---

## ✨ You're All Set!

Your SOMEWHERE website is ready to go. Just:

1. Set your Discord invite in `.env`
2. Run `python app.py` to test
3. Deploy to Render/Vercel
4. Share with your community!

**"1993. You are recording. The world does not care if you survive."**

---

Need help? Check:
- README.md for full docs
- SETUP.md for detailed setup
- GitHub Issues for bug reports

**Good luck with your launch! 🎬**

