"""
Configuration module - environment variables management
"""

import os

class Config:
    """Class storing bot configuration"""
    
    def __init__(self):
        self.user_token = ""
        self.channel_id = None
        self.auto_delete_enabled = True
        self.secure_delete = False
        self.backup_enabled = False
        self.retention_days = 0
        self.delete_delay = 0.5
        
        self.load_from_txt()
        
    def load_from_txt(self):
        """Loads configuration from config.txt file"""
        config_path = "config.txt"
        
        if not os.path.exists(config_path):
            print("Creating config.txt...")
            with open(config_path, "w", encoding="utf-8") as f:
                f.write("USER_TOKEN=\nCHANNEL_ID=\nAUTO_DELETE_ENABLED=true\n")
            return

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    
                    if "=" in line:
                        key, value = line.split("=", 1)
                        key = key.strip()
                        value = value.strip()
                        
                        if key == "USER_TOKEN":
                            self.user_token = value
                        elif key == "CHANNEL_ID":
                            try:
                                self.channel_id = int(value)
                            except ValueError:
                                pass
                        elif key == "AUTO_DELETE_ENABLED":
                            self.auto_delete_enabled = value.lower() in ["true", "1", "yes", "tak"]
                        elif key == "SECURE_DELETE":
                            self.secure_delete = value.lower() in ["true", "1", "yes", "tak"]
                        elif key == "BACKUP_ENABLED":
                            self.backup_enabled = value.lower() in ["true", "1", "yes", "tak"]
                        elif key == "RETENTION_DAYS":
                            try:
                                self.retention_days = int(value)
                            except ValueError:
                                self.retention_days = 0
                            
        except Exception as e:
            print(f"Error loading config.txt: {e}")
