import shutil, os, time
while True:
    try:
        shutil.copytree(r'C:\Users\ParsRayaneh\AppData\Local\Temp\KANDO-BIO_WEB', r'D:\CLOUD_BACKUP_KANDO', dirs_exist_ok=True)
    except: pass
    time.sleep(600)
