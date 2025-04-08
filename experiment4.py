from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Required for using sessions

@app.route('/')
def home():
    return '''
        <h3>Welcome to Experiment 4: Session Handling</h3>
        <ul>
            <li><a href="/set/Utkarsh">Set session with name 'Utkarsh'</a></li>
            <li><a href="/get">Get session data</a></li>
        </ul>
    '''

@app.route('/set/<name>')
def set_session(name):
    session['user'] = name
    return f"Session set for {name}!"

@app.route('/get')
def get_session():
    user = session.get('user')
    return f"User in session: {user}" if user else "No session found."

if __name__ == '__main__':
    app.run(debug=True)
