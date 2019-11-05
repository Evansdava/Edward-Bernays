from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/career')
def career():
    return render_template('career.html')


@app.route('/methods')
def methods():
    return render_template('methods.html')
