# Placeholder Images Guide

This folder needs the following images for the website to work properly:

## Required Images

### 1. `favicon.ico`
- **Size**: 32x32px or 16x16px
- **Format**: .ico
- **Description**: Browser tab icon
- **Suggestion**: Simple "S" logo in VHS red on black background

### 2. `og-image.png`
- **Size**: 1200x630px (Open Graph standard)
- **Format**: .png
- **Description**: Social media preview image
- **Content**: SOMEWHERE title with VHS aesthetic, dark background

### 3. `apple-touch-icon.png`
- **Size**: 180x180px
- **Format**: .png
- **Description**: iOS home screen icon
- **Content**: Same as favicon but higher resolution

## Gameplay Examples (in `examples/` folder)

### 4. `example1.png`
- **Recommended**: Facility exterior shot (establishing shot)
- **Caption**: "The facility appears abandoned."

### 5. `example2.png`
- **Recommended**: Mid-investigation shot (closer detail)
- **Caption**: "Something is moving behind the fence."

### 6. `example3.png`
- **Recommended**: Tense moment (danger encounter)
- **Caption**: "The guard's flashlight sweeps closer."

### 7. `example4.png`
- **Recommended**: Climactic or death moment
- **Caption**: "The tape cuts out here."

## How to Get Images from Your Bot

If you already have the SOMEWHERE Discord bot running:

```bash
# Navigate to your bot's cache directory
cd /path/to/somewhere-bot/cache

# Find good example frames
ls -lt *.png | head -20  # List recent images

# Copy to website
cp frame_001.png /path/to/website/static/images/examples/example1.png
cp frame_045.png /path/to/website/static/images/examples/example2.png
cp frame_089.png /path/to/website/static/images/examples/example3.png
cp frame_120.png /path/to/website/static/images/examples/example4.png
```

## Temporary Placeholders

Until you have real images, the website will show broken image icons.

To create quick SVG placeholders:

### Create a placeholder script:

```python
# create_placeholders.py
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(width, height, text, filename):
    img = Image.new('RGB', (width, height), color='#1A1A1A')
    draw = ImageDraw.Draw(img)
    
    # Try to use a monospace font
    try:
        font = ImageFont.truetype("cour.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Draw text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((width - text_width) / 2, (height - text_height) / 2)
    draw.text(position, text, fill='#E0E0E0', font=font)
    
    img.save(filename)
    print(f"Created: {filename}")

# Create placeholders
os.makedirs('static/images/examples', exist_ok=True)

create_placeholder(800, 600, "[TAPE CORRUPTED]\nFrame 001", 'static/images/examples/example1.png')
create_placeholder(800, 600, "[TAPE CORRUPTED]\nFrame 045", 'static/images/examples/example2.png')
create_placeholder(800, 600, "[TAPE CORRUPTED]\nFrame 089", 'static/images/examples/example3.png')
create_placeholder(800, 600, "[TAPE CORRUPTED]\nFrame 120", 'static/images/examples/example4.png')
create_placeholder(1200, 630, "SOMEWHERE\nAn Analog Horror Story", 'static/images/og-image.png')

print("Placeholders created! Replace with real images when available.")
```

Run with:
```bash
pip install pillow
python create_placeholders.py
```

## Image Optimization

Before deploying, optimize images for web:

```bash
# Install ImageMagick
brew install imagemagick  # macOS
# or download from https://imagemagick.org

# Optimize PNGs
cd static/images/examples
for img in *.png; do
    magick "$img" -resize 800x -quality 85 "optimized_$img"
done
```

## Recommended Tools

- **GIMP**: Free image editor
- **ImageMagick**: Command-line image processing
- **TinyPNG**: Online PNG compression
- **Favicon.io**: Generate favicons from text/image

---

**Note**: The website will still work without real images, but they're important for:
1. Social media sharing (og-image)
2. Demonstrating gameplay aesthetic
3. Conversion optimization (showing what the game looks like)

