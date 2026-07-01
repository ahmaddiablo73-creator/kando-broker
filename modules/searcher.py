import requests
class DataFetcher:
    def fetch(self, target):
        try:
            # اگر هدف فارسی است، اینجا می‌توانیم نگاشت (Mapping) داشته باشیم
            # اما برای تست، از یک URL عمومی‌تر استفاده می‌کنیم
            url = f"https://api.duckduckgo.com/?q={target.replace(' ', '+')}&format=json"
            response = requests.get(url, timeout=15)
            data = response.json()
            
            # منطقِ جستجویِ چندمرحله‌ای
            if data.get("Abstract"):
                return data["Abstract"]
            elif data.get("RelatedTopics"):
                # استخراج اولین نتیجه از موضوعات مرتبط
                return str(data["RelatedTopics"][0].get("Text", "No results found"))
            else:
                return "No data found for this specific query."
        except Exception as e:
            return f"Error: {str(e)}"