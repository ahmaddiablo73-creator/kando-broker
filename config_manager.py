import json
import os

class ConfigManager:
    def __init__(self, config_path="D:\KANDO-CORE\config.json"):
        self.config_path = config_path
        if not os.path.exists(config_path):
            self.save_config({"status": "initialized", "mode": "autonomous", "version": "1.0"})

    def save_config(self, data):
        with open(self.config_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_config(self):
        with open(self.config_path, "r") as f:
            return json.load(f)

config_manager = ConfigManager()
