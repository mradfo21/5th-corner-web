"""
R.A.S.T.E.R. - Flask Website
An Analog Horror Story

Phase 1: Simple landing page with room to grow
"""
from flask import Flask, render_template, jsonify
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Discord invite link (set as environment variable)
DISCORD_INVITE = os.environ.get('DISCORD_INVITE', 'https://discord.gg/YOUR_INVITE_CODE')

# Bot integration (for future phases)
BOT_ROOT = Path(__file__).parent.parent
STATE_FILE = BOT_ROOT / "state.json"
CACHE_DIR = BOT_ROOT / "cache"


@app.route('/')
def home():
    """Main landing page"""
    return render_template('index.html', discord_invite=DISCORD_INVITE)


@app.route('/health')
def health():
    """Health check for deployment monitoring"""
    return jsonify({'status': 'ok', 'phase': 1, 'version': '1.0.0'})


@app.errorhandler(404)
def not_found(e):
    """Custom 404 page - VHS themed"""
    return render_template('404.html', discord_invite=DISCORD_INVITE), 404


@app.errorhandler(500)
def internal_error(e):
    """Custom 500 page"""
    return render_template('404.html', discord_invite=DISCORD_INVITE), 500


if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)

