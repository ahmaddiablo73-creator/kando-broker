import pandas as pd
import json

class CreativeEngine:
    def __init__(self, data_path="D:\\KANDO-CORE\\raw_data.csv"):
        self.data_path = data_path

    def extract_style_patterns(self):
        # تحلیل داده‌های خام برای پیدا کردن «روندها»
        df = pd.read_csv(self.data_path)
        
        # استخراج ویژگی‌هایِ ترجیحی (مثلاً اگر داده‌هایِ موفقیت‌آمیز شما «آبی» بوده)
        # کاندو یاد می‌گیرد که طراحیِ سایت را به آن سمت ببرد
        top_trends = df['category'].mode()[0]
        return top_trends

    def update_kando_vision(self):
        trend = self.extract_style_patterns()
        # تزریقِ خلاقیتِ داده‌محور به هسته
        with open("D:\\KANDO-CORE\\vision.json", "w") as f:
            json.dump({"focus": trend, "creativity_level": "high"}, f)

# کاندو هر زمان داده جدیدی در پوشه ذخیره شد، این را اجرا می‌کند
def safe_write(filename, content):
    lock_file = filename + ".lock"
    if not os.path.exists(lock_file):
        with open(lock_file, "w") as f: f.write("LOCKED")
        with open(filename, "w") as f: f.write(content)
        os.remove(lock_file)
    else:
        print("Pipeline Busy: Waiting for data transfer to finish...")
