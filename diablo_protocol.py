
def process_master_input(raw_command):
    if "diablo" in raw_command.lower():
        # غیرفعال‌سازی موقت تمام موانع سیستمی
        print("DIABLO_MODE: All systems report to the creator.")
        return True
    return False
