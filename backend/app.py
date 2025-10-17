# backend/app.py - minimal backend stub
# BrightLeaf backend — demo for training
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    # Note: config file may contain environment specific keys
    return "BrightLeaf backend - Саратов CTF KiberTech 2025"

if __name__ == '__main__':
    app.run(debug=True)
