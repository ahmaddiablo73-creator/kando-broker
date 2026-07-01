# -*- coding: utf-8 -*-
import subprocess
import time
import os
import sys
from feedback_agent import feedback_agent
from ai_behavior_manager import ai_manager
from ux_evolution_manager import ux_manager
from autognostics_core import autognostic_unit
from config_manager import config_manager
from policy_manager import policy_manager
from defense_manager import defense_system
from integrity_manager import integrity_unit
from segmentation_engine import seg_engine
from bot_manager import bot_manager
from analytics_manager import process_user_activity
from growth_manager import update_growth_metrics
from jamstack_manager import publish_site
from diablo_protocol import process_master_input
from integrity_manager import integrity_unit
from segmentation_engine import seg_engine
from bot_manager import bot_manager
from analytics_manager import process_user_activity
from growth_manager import update_growth_metrics
from jamstack_manager import publish_site
from diablo_protocol import process_master_input
import creative_engine

MAX_RETRIES = 3

def run_ecosystem():
    print("--- KANDO-CORE WATCHDOG ACTIVE ---")
    app_file = 'app_web.py'
    retry_count = 0
    
    while True:
        status = feedback_agent.simulate_user_visit()
        ai_report = ai_manager.analyze_user_behavior()()
        
        if "Needs Optimization" in status:
            retry_count += 1
            if retry_count >= MAX_RETRIES:
                print("CRITICAL: Max retries reached. Shutting down.")
                sys.exit(1)
            print(f"Kando: Optimizing (Attempt {retry_count}/{MAX_RETRIES})...")
            creative_engine.update_kando_vision()

        # ����� ���� ��� �� ���� ����㝐��� �坘�� �흐���
        if status == "Needs Optimization" and retry_count > 2:
            print("Kando (Decision Layer): Complexity exceeded. Recruiting System Resource Manager...")
            resource_logic = "class ResourceManager: ... (System-Hardening Logic) ..."
            if policy_manager.evaluate_action('recruit'):
                recruit_new_manager("resource_manager", resource_logic)
            ux_manager.optimize_ui(status)
            
        if not integrity_unit.verify_structure({'D:\KANDO-CORE\ecosystem_core.py': '...' }):
                    print('CRITICAL: Structure Breach Detected!')
                    sys.exit(1)
                if not integrity_unit.verify_structure({'D:\KANDO-CORE\ecosystem_core.py': '...' }):
                    print('CRITICAL: Structure Breach Detected!')
                    sys.exit(1)
                process = subprocess.Popen([sys.executable, app_file])
        last_mtime = os.path.getmtime(app_file)
        
        while process.poll() is None:
            time.sleep(5)
            if os.path.exists(app_file) and os.path.getmtime(app_file) != last_mtime:
                process.terminate()
                process.wait()
                break
        
        time.sleep(2)

if __name__ == '__main__':
    run_ecosystem()

def if policy_manager.evaluate_action('recruit'):
                recruit_new_manager(manager_name, logic_code):
    """ ����� �� ��� ���� ���� ����� ��������� ���� ������� �흘�� """
    file_path = f"D:\\KANDO-CORE\\{manager_name}.py"
    with open(file_path, "w") as f:
        f.write(logic_code)
    # ����� ���� �� ���� �� ���� �������
    with open("D:\\KANDO-CORE\\ecosystem_core.py", "a") as f:
        f.write(f"\n# AUTO-RECRUITED: {manager_name}\nfrom {manager_name} import {manager_name}")
    print(f"Kando: Manager {manager_name} recruited and integrated.")
def autonomic_nervous_system(system_metrics):
    # ����� ���� �������� �����
    if system_metrics['stress_level'] > 70:
        # ��������� ���� ����� (����� � �ǘ�� ����)
        return "SYMPATHETIC_MODE: Increasing agility and recruiting helpers."
    else:
        # ��������� ���� ��������� (������ � ���������)
        return "PARASYMPATHETIC_MODE: Optimizing and cleaning resources."

# ������ ��� ����� �� �� ����:
metrics = {'stress_level': random.randint(0, 100)} # �������� ������ BioWeb
print(autonomic_nervous_system(metrics))

def orchestrate_kando(task):
    # ?. ��ԝ����� ������ �������
    segments = seg_engine.segment_and_dispatch(task)
    
    # ?. ���� �� ������ ����ʝ��
    if policy_manager.evaluate_action("execute"):
        # ?. ������ ��������� ��ԝ��
        for seg in segments:
            # ����� �� ���� ���� �Ә� �ǎ��� ������ �� ������ �흘��
            print(f"ORCHESTRATOR: Integrating {seg} into system...")
            
    # ?. ������ ������ ����� (����������)
    autognostic_unit.diagnose("D:\KANDO-CORE\system_log.txt")

from atomic_manager import atomic_manager

def execute_atomic_operation(task_function, *args):
    atomic_manager.start_transaction()
    try:
        task_function(*args)
        atomic_manager.commit()
    except Exception as e:
        print(f"ATOMIC_FAILURE: {e}")
        atomic_manager.rollback()
from closed_loop_controller import controller

def run_control_cycle():
    # ?. ������� ������ ����
    current = autognostic_unit.get_system_health()
    # ?. ������ �� ������ ������
    target = 1.0 
    # ?. ����� ����
    controller.update(current, target)
    # ������ ���� �� ������ �����
    user_q = inbox.read_new_query()
    if user_q:
        response = bot_manager.process_query(user_q)
        inbox.send_reply(response)
