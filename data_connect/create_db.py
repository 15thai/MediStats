import os
import pandas as pd
from sqlalchemy import create_engine


db_uri = os.environ['SQLALCHEMY_DATABASE_URI']

engine = create_engine(db_uri)

df = pd.read_csv("static/data/Medicare_Provider_Utilization_and_Payment_Data__Physician_and_Other_Supplier_PUF_CY2015.csv",dtype={'Zip Code of the Provider':str})

providers = df[['National Provider Identifier','Last Name/Organization Name of the Provider',
 'First Name of the Provider',
 'Middle Initial of the Provider',
 'Credentials of the Provider',
 'Gender of the Provider',
 'Entity Type of the Provider',
 'Street Address 1 of the Provider',
 'Street Address 2 of the Provider',
 'City of the Provider',
 'Zip Code of the Provider',
 'State Code of the Provider',
 'Country Code of the Provider',
 'Provider Type']]

providers = providers.drop_duplicates(subset=['National Provider Identifier','Last Name/Organization Name of the Provider',
 'First Name of the Provider',
 'Middle Initial of the Provider',
 'Credentials of the Provider',
 'Gender of the Provider',
 'Entity Type of the Provider',
 'Street Address 1 of the Provider',
 'Street Address 2 of the Provider',
 'City of the Provider',
 'Zip Code of the Provider',
 'State Code of the Provider',
 'Country Code of the Provider',
 'Provider Type'],keep='first')

providers.to_sql(name = 'providers', con = engine, if_exists = 'replace')


providers_pos =df.drop_duplicates(subset=['National Provider Identifier','Place of Service'])

providers_pos.to_sql(name = 'providers_pos', con = engine, if_exists = 'replace')


hcpcs = df[['HCPCS Code','HCPCS Description','HCPCS Drug Indicator']].drop_duplicates()

hcpcs.to_sql(name = 'hcpcs', con = engine, if_exists = 'replace')

puf_2015 = df[['National Provider Identifier','HCPCS Code','Number of Services',
 'Number of Medicare Beneficiaries',
 'Number of Distinct Medicare Beneficiary/Per Day Services',
 'Average Medicare Allowed Amount',
 'Average Submitted Charge Amount',
 'Average Medicare Payment Amount',
 'Average Medicare Standardized Amount']]

puf_2015.to_sql(name='puf_hcpcs_agg',con=engine, if_exists = 'replace')