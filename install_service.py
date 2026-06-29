import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import sys

# این اسکریپت باعث می‌شود کاندو به لیست سرویس‌های ویندوز اضافه شود
# کاندو در پس‌زمینه اجرا شده و با اینترنت هم قطع نمی‌شود
# فرمان برای اجرا: python install_service.py install