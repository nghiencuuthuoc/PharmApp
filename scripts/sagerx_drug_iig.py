
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-28: This code runs correctly


"""

import sys
sys.path.append('..')
import psycopg2
host = '192.168.48.129'
conn = psycopg2.connect(dbname='sagerx', host = '192.168.48.129', 
                        port = '5432', user = 'sagerx', password = 'sagerx')

curs = conn.cursor()
# drug_input = str(input("Enter name: "))
drug_name = str(input("Enter name: "))
# drug_name = drug_input.lower().replace(' ', '+').replace('-','+')

# Save file inactive_ingredient_list.txt
import os
print(drug_name)
drug_name_iig_file = drug_name + "_inactive_ingredient_list.csv"
drug_name_iig_file_path = os.path.join('../sagerxdata', drug_name_iig_file)
# table_name = str(input("Enter table name: "))
# sagerx_lake.orange_book_products
query = "SELECT * FROM sagerx_lake.orange_book_products WHERE ingredient LIKE '%" + drug_name + "%'"


fid = open(drug_name_iig_file_path, 'w')
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"

# print(sql)

curs.copy_expert(sql, fid)
fid.close()


# view data
import os

if os.path.isfile(drug_name_iig_file_path):
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df_iig = pd.read_csv(drug_name_iig_file_path)
    
    
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from pandasgui import show
    if df_iig is not None:
        drug_name = drug_name.replace('+',' ')
        df_iig_name = {drug_name :df_iig}
        show(**df_iig_name) # show data with pandasgui
else:
    print(f'Inactive ingredient {drug_name} not exist in iigdata!')




# SELECT * FROM sagerx_dev.int_mthspl_products_to_inactive_ingredients WHERE product_name LIKE '%tirzepatide%'


# table_name = str(input("Enter table name: "))
# csv_file = table_name + ".csv"
# query = "SELECT * FROM sagerx_lake." + table_name
# fid = open(csv_file, 'w')
# sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
# print(sql)