import sys, json
from modules.searcher import DataFetcher
from modules.analyzer import MarketAnalyzer
from modules.logger import SystemLogger

def main():
    # دریافت هدف مستقیماً از دستور پاورشل
    if len(sys.argv) < 2:
        print("[USAGE] python brain.py \"Target_Topic\"")
        return

    target = sys.argv[1]
    print(f"[SYSTEM] در حال پردازش دستور مستقیم برای: {target}")
    
    # اجرای مستقیم زنجیره عملیاتی
    data = DataFetcher().fetch(target)
    insight = MarketAnalyzer().process(data)
    SystemLogger().log(insight)
    
    print(f"[SUCCESS] گزارش عملیاتی برای '{target}' در mission_log.json ثبت شد.")

if __name__ == "__main__":
    main()