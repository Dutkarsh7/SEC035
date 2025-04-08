from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h3>Welcome to Experiment 3<br>Go to <a href="/login">/login</a></h3>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"Welcome, {user}!"
    return '''
        <h2>Experiment 3: Login Form</h2>
        <form method="post">
            Username: <input name="username">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
