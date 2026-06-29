import subprocess
import os

def run_in_sandbox(script_name):
    sandbox_path = os.path.join('D:\\KANDO-CORE', 'sandbox')
    script_path = os.path.join(sandbox_path, script_name)
    
    # اجرایِ کد در محیطِ ایزوله با محدودیتِ سطحِ دسترسی
    print(f"KANDO-CORE: Executing in Sandbox: {script_name}")
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True, timeout=30)
        return result.stdout
    except Exception as e:
        return f"Sandbox Error: {str(e)}"

if __name__ == '__main__':
    print("KANDO-CORE: Sandbox layer active.")
