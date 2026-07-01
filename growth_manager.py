from growth_dashboard import growth_dashboard

def update_growth_metrics(new_data):
    # کاندو داده‌های جدید را تحلیل کرده و داشبورد را آپدیت می‌کند
    growth_dashboard.metrics.update(new_data)
    growth_dashboard.display_report()
