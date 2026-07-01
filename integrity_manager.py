import hashlib

class IntegrityManager:
    def __init__(self, core_path="D:\KANDO-CORE"):
        self.core_path = core_path

    def calculate_hash(self, file_path):
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def verify_structure(self, file_map):
        # بررسی اینکه آیا تمامِ فایل‌های دژ دقیقاً همان هستند که باید باشند
        for file, original_hash in file_map.items():
            if self.calculate_hash(file) != original_hash:
                return False
        return True

integrity_unit = IntegrityManager()
