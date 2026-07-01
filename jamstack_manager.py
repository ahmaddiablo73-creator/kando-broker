from jamstack_builder import jamstack_engine

def publish_site():
    # جمع‌آوری داده‌ها از موتور پیشنهاددهنده و ایجاد سایت
    data = {"index": "Welcome to BioWeb", "movies": "List of recommended movies"}
    jamstack_engine.build_static_site(data)
