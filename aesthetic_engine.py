import random

class AestheticEngine:
    def __init__(self):
        # پالت رنگیِ مدرن و حرفه‌ای
        self.palettes = {
            "modern_dark": {"bg": "#121212", "accent": "#BB86FC", "text": "#E0E0E0"},
            "professional_blue": {"bg": "#F4F7F6", "accent": "#2D3436", "text": "#0984E3"}
        }
        self.current_theme = "modern_dark"

    def generate_ui_blueprint(self, component_type):
        """تولیدِ استایلِ حرفه‌ای برای هر کامپوننت"""
        theme = self.palettes[self.current_theme]
        if component_type == "dashboard":
            return f"border-radius: 12px; background-color: {theme['bg']}; box-shadow: 0 4px 20px rgba(0,0,0,0.3);"
        if component_type == "button":
            return f"padding: 10px 20px; background: {theme['accent']}; border: none; border-radius: 8px; color: white;"
        return ""

# این موتور را به هسته کاندو تزریق می‌کنیم
engine = AestheticEngine()