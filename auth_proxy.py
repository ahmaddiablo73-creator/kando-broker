from auth_module import KandoAuth

def secure_action(user, action):
    auth = KandoAuth()
    if auth.check_access(user, action):
        return "ACTION_PERMITTED"
    else:
        return "ACCESS_DENIED"
