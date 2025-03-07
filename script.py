import pandas as pd
from dbconnector import DataBaseConnector

db_coonect = DataBaseConnector('ODOO')

sql  = '''
select name, email, phone, is_company from res_partner
'''

data_df = db_coonect.get_dataframe_from_postgres(sqlquery=sql,sqlparams=None)

data_df.loc[data_df['email']==''].to_excel('missing_email.xlsx')
data_df.loc[data_df['phone']==''].to_excel('missing_phones.xlsx')