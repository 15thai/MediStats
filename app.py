from flask import Flask, render_template, request
from jinja2 import Environment

import pandas as pd



app = Flask(__name__)

# Index page
@app.route('/')
def index():
    """
    Welcome page of MediStats
    """    
    return render_template("index.html",)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)