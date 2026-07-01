import sys

def main():
    print("KANDO-CORE > READY. I AM LISTENING.")
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            
            cmd = line.strip().lower()
            if cmd == "exit": break
            
            # منطقِ تعامل (هوشِ پایه)
            if "where are you" in cmd:
                print("KANDO-CORE > I AM INSIDE YOUR SYSTEM, D:\\KANDO-CORE.")
            elif "who are you" in cmd:
                print("KANDO-CORE > I AM THE CORE, EXECUTING YOUR WILL.")
            elif "hi" in cmd or "hello" in cmd:
                print("KANDO-CORE > GREETINGS. I AM ONLINE.")
            else:
                # اگر فرمانِ خاصی نبود، فقط تأیید می‌کند که شنیده است
                print(f"KANDO-CORE > RECEIVED: {cmd.upper()}. STANDING BY.")
                
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()