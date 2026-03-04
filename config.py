"""
Configuration module for Project Lazarus Feed.
Centralized configuration management with environment variable support.
"""
import os
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class DeepSeekConfig:
    """Configuration for DeepSeek AI model integration"""
    api_key: str = field(default_factory=lambda: os.getenv("DEEPSEEK_API_KEY", ""))
    base_url: str = field(default_factory=lambda: os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    model: str = "deepseek-chat"
    max_tokens: int = 2048
    temperature: float = 0.7
    timeout: int = 30
    max_retries: int = 3

@dataclass
class FirebaseConfig:
    """Configuration for Firebase integration"""
    service_account_path: str = field(default_factory=lambda: os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "./firebase-credentials.json"))
    project_id: str = field(default_factory=lambda: os.getenv("FIREBASE_PROJECT_ID", ""))
    collection_name: str = "lazarus_feed"
    batch_size: int = 10

@dataclass
class LoggingConfig:
    """Configuration for logging system"""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: str = "./logs/lazarus_feed.log"
    max_bytes: int = 10485760  # 10MB
    backup_count: int = 5

@dataclass
class FeedConfig:
    """Configuration for feed generation"""
    feed_name: str = "Project Lazarus"
    refresh_interval_minutes: int = 60
    max_items_per_run: int = 50
    categories: list = field(default_factory=lambda: ["technology", "ai", "programming", "science"])
    quality_threshold: float = 0.7

class ConfigManager:
    """Singleton configuration manager"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance