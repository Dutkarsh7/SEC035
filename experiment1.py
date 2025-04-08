from flask import Flask, request

app = Flask(__name__)

@app.route('/form')
def form():
    return '''
        <h2>Experiment 1: Simple Form (GET)</h2>
        <form action="/result" method="get">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''

@app.route('/result')
def result():
    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
