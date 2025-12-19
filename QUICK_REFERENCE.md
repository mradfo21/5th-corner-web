# SOMEWHERE Website - Quick Reference Card

## 🚀 Common Commands

```bash
# Start development server
python app.py

# Generate placeholder images
python create_placeholders.py

# Install dependencies
pip install -r requirements.txt

# Check Flask version
python -c "import flask; print('Flask installed')"
```

## 📁 File Locations

```
Key Files:
├── app.py                          # Main Flask app
├── .env                            # Environment variables (YOUR_DISCORD_INVITE here!)
├── templates/index.html            # Main page content (edit copy here)
├── static/css/style.css            # VHS styling (edit colors here)
├── static/images/examples/         # Replace with real images
└── README.md                       # Full documentation

Documentation:
├── GETTING_STARTED.md              # Quick start (START HERE)
├── SETUP.md                        # Detailed setup
├── PROJECT_SUMMARY.md              # Technical overview
└── QUICK_REFERENCE.md              # This file
```

## 🔧 Quick Edits

### Change Discord Invite
**File:** `.env`
```bash
DISCORD_INVITE=https://discord.gg/YOUR_NEW_INVITE
```

### Change Hero Text
**File:** `templates/index.html`
```html
<h1 class="hero-title">SOMEWHERE</h1>
<p class="hero-tagline">Your new tagline here</p>
```

### Change Main Color
**File:** `static/css/style.css`
```css
:root {
    --color-vhs-red: #FF0033;  /* Change this */
}
```

### Disable Scanlines
**File:** `static/css/style.css`
```css
:root {
    --scanline-opacity: 0;  /* Was 0.05 */
}
```

## 🌐 URLs

```bash
Local Development:
http://localhost:5000               # Main page
http://localhost:5000/health        # Health check

After Deployment (Render):
https://somewhere-website.onrender.com          # Your site
https://dashboard.render.com                    # Dashboard
```

## 🎨 Color Palette

```css
--color-black: #000000           /* Pure black */
--color-near-black: #0A0A0A      /* Background */
--color-dark-gray: #1A1A1A       /* Sections */
--color-gray: #2A2A2A            /* Cards */
--color-off-white: #E0E0E0       /* Text */
--color-vhs-red: #FF0033         /* Accent (VHS) */
--color-phosphor-green: #00FF41  /* Accent (CRT) */
```

## 📦 Dependencies

```
Flask==3.0.0          # Web framework
gunicorn==21.2.0      # Production server
python-dotenv==1.0.0  # Environment variables
pillow                # Image generation (optional)
```

## 🚀 Deployment Quick Links

### Render.com
- Dashboard: https://dashboard.render.com
- Docs: https://render.com/docs/web-services
- **Cost:** Free tier or $7/month

### Vercel
- Dashboard: https://vercel.com/dashboard
- Docs: https://vercel.com/docs
- **Cost:** Free for personal

### Heroku
- Dashboard: https://dashboard.heroku.com
- Docs: https://devcenter.heroku.com
- **Cost:** ~$7/month (no free tier)

## 🖼️ Image Specs

```
Gallery Images (4 required):
- Location: static/images/examples/
- Names: example1.png, example2.png, example3.png, example4.png
- Size: 800x600px recommended
- Format: PNG or JPEG

Social Media:
- OG Image: static/images/og-image.png (1200x630px)
- Favicon: static/images/favicon.ico (32x32px)
- Apple Icon: static/images/apple-touch-icon.png (180x180px)
```

## ⚡ Quick Fixes

### Port already in use
```python
# In app.py, change port:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module not found
```bash
pip install Flask gunicorn python-dotenv
```

### Images not loading
```bash
# Check files exist
dir static\images\examples\  # Windows
ls static/images/examples/   # macOS/Linux

# Regenerate placeholders
python create_placeholders.py
```

### Styles not updating
```
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Check browser console (F12) for errors
```

## 📊 Performance Targets

```
Page Load Time: < 2 seconds
Time to Interactive: < 3 seconds
Lighthouse Score: 90+

Image Sizes:
- Gallery images: < 500KB each
- OG image: < 300KB
- Total page weight: < 2MB
```

## 🔐 Environment Variables

```bash
Required:
DISCORD_INVITE=https://discord.gg/YOUR_CODE
SECRET_KEY=your-secret-key-here

Optional:
FLASK_ENV=development
BOT_STATE_FILE=/path/to/state.json      # Phase 2
BOT_CACHE_DIR=/path/to/cache            # Phase 2
```

## 🧪 Testing Checklist

```
[ ] Homepage loads without errors
[ ] Discord button works (opens in new tab)
[ ] All 4 gallery images display
[ ] Mobile responsive (test on phone)
[ ] Works in Chrome, Firefox, Safari, Edge
[ ] Scanlines visible but subtle
[ ] No console errors (F12 → Console)
[ ] Page loads in < 3 seconds
```

## 📱 Browser Support

```
✅ Chrome 120+
✅ Firefox 120+
✅ Safari 17+
✅ Edge 120+
✅ Mobile Safari (iOS 15+)
✅ Chrome Mobile (Android)
```

## 🆘 Emergency Contacts

```
Documentation:
- README.md (full docs)
- GETTING_STARTED.md (quick start)
- SETUP.md (detailed setup)

Flask Docs:
- https://flask.palletsprojects.com

Community:
- Your Discord server
- GitHub Issues
```

## 🎯 Phase Roadmap

```
Phase 1 (Current): ✅ COMPLETE
- Landing page
- VHS aesthetic
- Discord CTA
- Placeholder images

Phase 2 (Future):
- Live stats from bot
- Real-time gallery
- API endpoints

Phase 3 (Future):
- Web-based gameplay
- User accounts
- Tape library
- Community features
```

## 💡 Pro Tips

```
1. Use permanent Discord invites (never expire)
2. Optimize images before adding (< 500KB each)
3. Test on mobile early and often
4. Keep page load time under 2 seconds
5. Replace placeholders with real gameplay ASAP
6. Monitor with UptimeRobot (free)
7. Add analytics (Google Analytics or Plausible)
8. Use custom domain for professionalism
```

## 🔗 Useful Links

```
Create Favicon:
- https://favicon.io
- https://realfavicongenerator.net

Optimize Images:
- https://tinypng.com
- https://squoosh.app

Test Performance:
- https://pagespeed.web.dev
- https://gtmetrix.com

Test Mobile:
- https://responsivedesignchecker.com
```

---

## 🎬 Launch Sequence

```
1. ✅ Set DISCORD_INVITE in .env
2. ✅ Run python app.py (test locally)
3. ✅ Replace placeholder images (optional but recommended)
4. ✅ Push to GitHub
5. ✅ Deploy to Render/Vercel
6. ✅ Test production site
7. ✅ Share with community
8. ✅ Monitor performance
```

---

**Need more details?** See GETTING_STARTED.md or README.md

**"1993. You are recording. The world does not care if you survive."**

