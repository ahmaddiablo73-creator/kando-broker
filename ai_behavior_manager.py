import random

class AIBehaviorManager:
    def __init__(self):
        self.metrics = ["click_rate", "bounce_rate", "session_duration"]

    def analyze_user_behavior(self):
        # شبیه‌سازی تحلیلِ رفتارِ واقعیِ کاربر
        insight = random.choice(self.metrics)
        data = random.randint(10, 90)
        report = f"[AI_BEHAVIOR_REPORT] Metric: {insight}, Value: {data}%"
        
        # ثبت گزارش برای هسته‌یِ کاندو
        with open("D:\KANDO-CORE\system_log.txt", "a") as f:
            f.write(f"\n{report}")
        return report

ai_manager = AIBehaviorManager()
