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
    """
    Return 5 providers based on zipcode
    """
    if request.method == 'POST':
        zip_code = request.form.getlist('zip_code')[0]

        # Reinitialize DB Connection
        con = engine.connect()
        md_list = pd.read_sql(db_query.sql_providers_in_zip(zip_code=zip_code),con).head()

        return render_template("index.html", md_list=md_list)

# Index page
@app.route('/')
def index():
    """
    Welcome page of MediStats
    """ 
    # Initialize DB Connection
    con = engine.connect()   
    md_list = pd.read_sql(db_query.sql_providers_in_zip(zip_code='22903'),con).head()

    return render_template("index.html",md_list=md_list)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)