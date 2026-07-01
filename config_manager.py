import json

def update_mission(mission_data):
    with open('mission_config.json', 'w') as f:
        json.dump(mission_data, f, indent=4)
    print("Mission configuration updated successfully.")

# تنظیمات پیش‌فرض برای تست
default_mission = {
    "task_id": "FISH_MARKET_ANALYSIS_001",
    "target": "بازار ماهی تهران",
    "objective": "تحلیل روند تقاضا برای هفته آینده",
    "status": "READY"
}

if __name__ == "__main__":
    update_mission(default_mission)