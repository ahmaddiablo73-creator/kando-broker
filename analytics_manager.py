from recommendation_engine import recommendation_engine

def process_user_activity(user_id, action):
    # کاندو داده را تحلیل کرده و رفتار را دسته‌بندی می‌کند
    recommendation_engine.analyze_behavior(user_id, action['movie'], action['rating'])
