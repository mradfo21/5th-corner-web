"""
Flask configuration
"""
import os
from pathlib import Path

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    DISCORD_INVITE = os.environ.get('DISCORD_INVITE') or 'https://discord.gg/YOUR_INVITE_CODE'
    
    # Bot integration paths (for Phase 2+)
    BOT_STATE_FILE = os.environ.get('BOT_STATE_FILE')
    BOT_CACHE_DIR = os.environ.get('BOT_CACHE_DIR')
    
    # Flask settings
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0  # Disable caching in development


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year cache in production


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

