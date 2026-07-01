class PolicyManager:
    def __init__(self):
        self.policies = {
            "max_autonomy": True,
            "cost_optimization": True,
            "safety_protocol": "strict"
        }

    def evaluate_action(self, action_name):
        # بررسی اینکه آیا اقدامِ کاندو با سیاست‌هایِ فرمانده همخوانی دارد؟
        if action_name == "delete_all" and self.policies["safety_protocol"] == "strict":
            return False
        return True

policy_manager = PolicyManager()
