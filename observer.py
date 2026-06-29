from evolution_engine import KandoEvolution

def evolve_to_interactive():
    kando = KandoEvolution('app_web.py')
    new_ui = """
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['command']
        return f'<h1>KANDO-CORE RECEIVED: {user_input}</h1><a href="/">BACK</a>'
    return '''
        <h1>KANDO-CORE INTERACTIVE</h1>
        <form method="POST">
            <input type="text" name="command" placeholder="Enter evolution command...">
            <input type="submit" value="EXECUTE">
        </form>
    '''
if __name__ == '__main__':
    app.run(port=5000)
"""
    kando.self_mutate(new_ui)

if __name__ == '__main__':
    evolve_to_interactive()
