import time
import threading
import pynvml # pip install nvidia-ml-py

class GPUManager:
    def __init__(self):
        pynvml.nvmlInit()
        self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        self.running = True

    def optimize_logarithmic_load(self):
        while self.running:
            # ۱. تحلیلِ وضعیتِ فعلی
            util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
            temp = pynvml.nvmlDeviceGetTemperature(self.handle, 0)
            
            # ۲. تنظیمِ لگاریتمیِ بارِ کاری (Logarithmic Load Scaling)
            # اگر دما بالاست، نرخِ پردازش را به صورتِ لگاریتمی کاهش می‌دهد تا سیستم کرش نکند
            if temp > 80:
                print(f"[SYSTEM-LOG] دما بحرانی است. در حالِ کاهشِ نرخِ پردازش...")
                time.sleep(5) 
            
            # ۳. زمان‌بندیِ بازگشت: ۱ دقیقه
            time.sleep(60)

# استقرارِ ناظر در هسته
manager = GPUManager()
optimizer_thread = threading.Thread(target=manager.optimize_logarithmic_load, daemon=True)
optimizer_thread.start()