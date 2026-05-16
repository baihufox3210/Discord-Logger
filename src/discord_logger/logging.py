import os
import requests

from enum import IntEnum
from datetime import datetime, timezone

class Color(IntEnum):
    SUCCESS = 0x2ECC71
    DEBUG = 0x95A5A6
    INFO = 0x3498DB
    WARNING = 0xF1C40F
    ERROR = 0xE74C3C
    CRITICAL = 0x992D22

class DiscordLogger:
    def __init__(self, webhook_url: str, timeout: int = 5, owner_name: str = "baihu", webhook_name: str = "logging", owner_avatar: str = None, webhook_avatar: str = None):
        self.webhook_url = webhook_url
        if not self.webhook_url: raise ValueError("discord webhook url is missing")
        
        self.owner_name = owner_name
        self.owner_avatar = owner_avatar or os.getenv("DISCORD_OWNER_AVATAR_URL")
        
        self.webhook_name = webhook_name
        self.webhook_avatar = webhook_avatar or os.getenv("DISCORD_WEBHOOK_AVATAR_URL")
        
        self.timeout = timeout
        
    def _truncate(self, text: str, limit: int) -> str:
        if len(text) <= limit: return text
        return text[:limit - 3].rstrip() + "..."
        
    def _send(self, title: str, description: str, color: Color):
        title = self._truncate(title, 256)
        description = self._truncate(description, 4000)
        
        payload = {
            "username": self.webhook_name,
            "avatar_url": self.webhook_avatar,
            "embeds": [
                {
                    "title": title, "description": description, "color": color,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "footer": {
                        "text": self.owner_name,
                        "icon_url": self.owner_avatar
                    }
                }
            ]
        }
        
        try: requests.post(self.webhook_url, json = payload, timeout = self.timeout)
        except Exception as e: print(e)
        
    def success(self, title: str, description: str):
        self._send(title = title, description = description, color = Color.SUCCESS)
        
    def debug(self, title: str, description: str):
        self._send(title = title, description = description, color = Color.DEBUG)
        
    def info(self, title: str, description: str):
        self._send(title = title, description = description, color = Color.INFO)
        
    def warning(self, title: str, description: str):
        self._send(title = title, description = description, color = Color.WARNING)
        
    def error(self, title: str, description: str):
        self._send(title = title, description = description, color = Color.ERROR)

    def critical(self, title: str, description: str):
        self._send(title = title, description = description, color = Color.CRITICAL)