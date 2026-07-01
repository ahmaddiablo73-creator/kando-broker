# KANDO ACCESS CONTROL MODULE
class KandoAuth:
    def __init__(self):
        self.users = {"admin": "root_level", "user": "read_only"}

    def check_access(self, username, action):
        role = self.users.get(username, "guest")
        if role == "root_level":
            return True
        if role == "read_only" and action == "view":
            return True
        return False

# تستِ نفوذِ مجوز
auth = KandoAuth()
print(f"DIABLO: Access granted: {auth.check_access('user', 'view')}")