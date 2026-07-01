class MarketAnalyzer:
    def process(self, data):
        return f"تحلیل استخراجی: " + data[:200]

class MarketAnalyzer:
    def process(self, data):
        # اگر دیتای دریافتی موجود باشد، آن را پردازش کن
        if not data or data == "No data found.":
            return "تحلیل استخراجی: داده‌ای یافت نشد."
        # بازگرداندن داده برای ثبت در لاگ
        return f"تحلیل استخراجی: {data[:200]}"