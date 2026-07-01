import sys

# سیستمِ آفلاین: بدون وابستگی به اینترنت
def kando_offline():
    print("KANDO-CORE: OFFLINE MODE ACTIVATED. NO EXTERNAL CONNECTION.")
    while True:
        try:
            cmd = input("KANDO > ")
            if cmd.lower() == "exit": break
            # پردازشِ داخلی
            print(f"INTERNAL PROCESSED: {cmd[::-1]}") # مثال: معکوس کردن متن برای نمایشِ پردازشِ محلی
        except EOFError: break

if __name__ == "__main__":
    kando_offline()