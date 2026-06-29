# استفاده از هسته‌یِ پایه برای کاندو
FROM mcr.microsoft.com/powershell:latest

# تعیینِ مسیرِ عملیاتی در کانتینر
WORKDIR /app

# کپیِ هسته‌یِ تکامل‌یافته به محیطِ جدید
COPY . .

# اجرایِ خودکارِ هسته پس از استقرار
CMD ["pwsh", "-File", "Kando_Kernel_v2.ps1"]