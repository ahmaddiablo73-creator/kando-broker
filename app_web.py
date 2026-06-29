
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return "<h1>SYSTEM EVOLVED: Build a beautiful UI.</h1><a href='/'>BACK</a>"
    return """<h1>KANDO-CORE v3.0</h1><p>Status: Build a beautiful UI.</p><form method='POST'><input name='command'><input type='submit'></form>"""
if __name__ == '__main__':
    app.run(port=5000)
from aesthetic_engine import engine

# هنگام تولیدِ HTML، از انجین کمک می‌گیرد:
def render_component(name):
    style = engine.generate_ui_blueprint(name)
    return f'<div style="{style}">Content for {name}</div>'