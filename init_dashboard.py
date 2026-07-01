import json
import psutil
import os

def get_dashboard_data():
    path = r'C:\Users\User\Documents\KANDO_BIO_WEB\src\assets\metrics.json'
    data = {
        'cpu': psutil.cpu_percent(),
        'ram': psutil.virtual_memory().percent,
        'status': 'OPERATIONAL'
    }
    with open(path, 'w') as f:
        json.dump(data, f)
    print('DIABLO: Metrics injected into dashboard.')

get_dashboard_data()
