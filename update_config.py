import os
new_path = os.path.expanduser(r"~\Documents\KANDO_BIO_WEB")
with open(r"D:\KANDO-CORE\config.py", "w") as f:
    f.write(f"PROJECT_ROOT = r'{new_path}'")
print(f"CORE: System relocated to {new_path}")
