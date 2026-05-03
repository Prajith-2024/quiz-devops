from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def quiz():
    return '''
    <form action="/submit" method="post">
        2+2 = ?
        <input type="radio" name="q1" value="3">3
        <input type="radio" name="q1" value="4">4
        <input type="submit">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    if request.form.get("q1") == "4":
        score += 1
    return f"Score: {score}"

@app.route('/metrics')
def metrics():
    return "quiz_users 5"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)