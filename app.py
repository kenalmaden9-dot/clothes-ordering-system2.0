from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Clothes Ordering System</h1>"
