#
"""
The neessary files should be installed with python pip install -r requirements.txs
"""
import os

from flask import Flask, render_template, request
from jinja2 import Environment
from sqlalchemy import create_engine

import pandas as pd

from data_connect import db_query


app = Flask(__name__)

db_uri = os.environ['SQLALCHEMY_DATABASE_URI']

engine = create_engine(db_uri)

# Get Doctors in Zip Code

@app.route('/zip_code',methods=['POST','GET'])
def get_zip_list():
    if request.method == 'POST':
        zip_code = request.form.getlist('zip_code')

        # Reinitialize DB Connection
        con = engine.connection()
        provider_data = pd.read_sql(db_query.sql_providers_in_zip(zip_code=zip_code),bc)
        return render_template("provider_list.html", provider_list=provider_data.to_html())

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