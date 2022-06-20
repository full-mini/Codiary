from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("login.html")


@app.route('/signin')
def detail():
    return render_template("signin.html")

@app.route('/main')
def detail():
    return render_template("main.html")



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)