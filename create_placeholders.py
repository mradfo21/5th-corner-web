"""
Create placeholder images for SOMEWHERE website
Run this if you don't have real gameplay images yet
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(width, height, text, filename, bg_color='#1A1A1A', text_color='#E0E0E0'):
    """Create a simple placeholder image with text"""
    
    # Create image with dark background
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a monospace font, fall back to default
    font_size = 36
    try:
        font = ImageFont.truetype("cour.ttf", font_size)  # Courier New on Windows
    except:
        try:
            font = ImageFont.truetype("Courier New.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Courier.dfont", font_size)  # macOS
            except:
                print(f"Warning: Using default font for {filename}")
                font = ImageFont.load_default()
    
    # Draw text centered
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((width - text_width) / 2, (height - text_height) / 2)
    
    # Draw VHS-style border
    draw.rectangle([10, 10, width-10, height-10], outline='#FF0033', width=2)
    
    # Draw text
    draw.text(position, text, fill=text_color, font=font)
    
    # Add "REC" indicator
    rec_font_size = 24
    try:
        rec_font = ImageFont.truetype("cour.ttf", rec_font_size)
    except:
        rec_font = font
    
    draw.text((20, 20), "▶ REC", fill='#FF0033', font=rec_font)
    
    # Save
    img.save(filename)
    print(f"[OK] Created: {filename}")


def main():
    """Create all placeholder images"""
    
    print("Creating placeholder images for SOMEWHERE website...")
    print("-" * 60)
    
    # Create directories if they don't exist
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('static/images/examples', exist_ok=True)
    
    # Example gameplay images
    placeholders = [
        {
            'width': 800,
            'height': 600,
            'text': '[TAPE CORRUPTED]\n\nFrame 001\nFacility Exterior',
            'filename': 'static/images/examples/example1.png'
        },
        {
            'width': 800,
            'height': 600,
            'text': '[TAPE CORRUPTED]\n\nFrame 045\nPerimeter Fence',
            'filename': 'static/images/examples/example2.png'
        },
        {
            'width': 800,
            'height': 600,
            'text': '[TAPE CORRUPTED]\n\nFrame 089\nGuard Encounter',
            'filename': 'static/images/examples/example3.png'
        },
        {
            'width': 800,
            'height': 600,
            'text': '[SIGNAL LOST]\n\nFrame 120\nTape Ends',
            'filename': 'static/images/examples/example4.png'
        }
    ]
    
    # Create example images
    for placeholder in placeholders:
        create_placeholder(
            placeholder['width'],
            placeholder['height'],
            placeholder['text'],
            placeholder['filename']
        )
    
    # Create OG image for social media
    create_placeholder(
        1200,
        630,
        'SOMEWHERE\n\nAn Analog Horror Story\n\n1993',
        'static/images/og-image.png'
    )
    
    # Create simple favicon (will need to convert to .ico manually)
    create_placeholder(
        180,
        180,
        'S',
        'static/images/apple-touch-icon.png'
    )
    
    print("-" * 60)
    print("[OK] All placeholders created!")
    print()
    print("Next steps:")
    print("1. Replace these with real gameplay images from your bot")
    print("2. Convert apple-touch-icon.png to favicon.ico")
    print("   - Use online tool: favicon.io or convertio.co")
    print("3. Update captions in templates/index.html if needed")
    print()
    print("Run 'python app.py' to start the development server")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        print()
        print("Make sure PIL/Pillow is installed:")
        print("  pip install pillow")

