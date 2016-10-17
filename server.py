from flask import Flask, render_template

app = Flask('Calculator')


@app.route("/")
def index():
    return render_template('calculator.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9999)