import subprocess
import time
import sys
import os

import creative_engine
import feedback_agent

# در حلقه ی اصلیِ اکوسیستم
def sync_data_to_creativity():
    creative_engine.update_kando_vision()
    # کاندو فایلِ vision.json را می‌خواند و استایلِ سایت را متحول می‌کند

def kando_marketing_autonomy():
    # ۱. کاندو از vision.json می‌فهمد چه پیامی ترند است
    # ۲. دستورِ ساختِ بنر را به BannerBrain می‌دهد
    msg = "فروش ویژه ماهی تازه" # این پیام را از داده‌های خام می‌گیرد
    brain.design_banner(msg)

def run_ecosystem():
    print("--- KANDO-CORE WATCHDOG ACTIVE ---")
    app_file = 'app_web.py'
    
    # در حلقه ی اصلیِ اکوسیستم
while True:
    # ۱. کاندو سایت را تغییر می‌دهد
    # ۲. فیدبک ایجنت بازدید می‌کند
    status = feedback_agent.simulate_user_visit()
    
    # ۳. اگر فیدبک منفی بود، کاندو کد را در سندباکس اصلاح می‌کند
    if "Needs Optimization" in status:
        print("Kando: Optimizing based on user feedback...")
        # دستور اصلاح خودکار اجرا می‌شود

    while True:
        # اجرای هسته در یک پروسه مجزا
        process = subprocess.Popen([sys.executable, app_file])
        
        # مانیتور کردن وضعیت فایل برای تغییرات (تکامل)
        last_mtime = os.path.getmtime(app_file)
        
        while process.poll() is None:
            time.sleep(1)
            # اگر کاندو خودش را بازنویسی کرد (تغییر زمان فایل)
            if os.path.getmtime(app_file) != last_mtime:
                print("--- EVOLUTION DETECTED: RESTARTING SYSTEM ---")
                process.terminate()
                break
        
        time.sleep(1) # وقفه ایمنی

import subprocess

def auto_commit_changes():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Kando-Auto-Evolution: Updated UI/Logic based on data feedback."], check=True)
    except Exception as e:
        print(f"Git auto-commit failed: {e}")

# این تابع در انتهای هر چرخه تکامل توسط کاندو فراخوانی می‌شود

if __name__ == '__main__':
    run_ecosystem()
