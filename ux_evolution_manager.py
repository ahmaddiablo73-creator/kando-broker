import json
import os

class UXEvolutionManager:
    def __init__(self, target_dir):
        self.target_dir = target_dir

    def optimize_ui(self, feedback):
        # تحلیل بازخورد و تغییر استایل
        if "positive" in feedback:
            # اگر بازخورد مثبت بود، پالت رنگی را تقویت کن
            print("UX_MANAGER: Optimizing interface for user delight...")
            self.apply_style("gold_accent")
        else:
            # اگر منفی بود، خوانایی را بهبود ببخش
            self.apply_style("high_contrast")

    def apply_style(self, style_name):
        style_path = os.path.join(self.target_dir, "style.css")
        # تزریق استایل جدید به فایلِ CSS در دایرکتوریِ BioWeb
        with open(style_path, "w") as f:
            f.write(f"/* Kando-UX-Evolution: {style_name} applied */\nbody {{ background: #f4f4f4; }}")

ux_manager = UXEvolutionManager("D:\BIO-WEB")
