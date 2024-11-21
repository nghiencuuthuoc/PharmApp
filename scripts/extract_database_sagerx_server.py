#!/usr/bin/env python
# coding: utf-8

# <a href="https://github.com/nghiencuuthuoc/PharmApp/PharmApp.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
# 
# ![](./images/PharmApp-logo.png)
# # PharmApp - Research and Development Pharmaceuticals
# Copyright 2024 | Nghiên Cứu Thuốc | RD_Pharma_Plus
# 
# Email: nghiencuuthuoc@gmail.com | nghiencuuthuoc.com | x.com/nghiencuuthuoc | facebook.com/nghiencuuthuoc

# ## Connect to psql

# In[5]:


import sys
sys.path.append('..')
# import os
# os.getcwd()


# In[ ]:


# SAGERX_FOLDER = '../sagerxdata'


# ## all_tables

# In[130]:


table_name = 'all_tables'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = 'SELECT * FROM pg_catalog.pg_tables'
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
all_tables = pd.read_csv(path_csv_file, low_memory=False)
sagerx_lake_tables = all_tables[all_tables["schemaname"] == 'sagerx_lake']
sagerx_lake_tables = sagerx_lake_tables.drop(['tableowner','tablespace', 'hasindexes','hastriggers', 'rowsecurity', 'hasrules'], axis=1)
sagerx_lake_tables = sagerx_lake_tables.set_axis(range(len(sagerx_lake_tables)))
sagerx_lake_tables


# In[133]:


sagerx_tables = all_tables[all_tables["schemaname"] == 'sagerx']
sagerx_tables = sagerx_tables.drop(['tableowner','tablespace', 'hasindexes','hastriggers', 'rowsecurity', 'hasrules'], axis=1)
sagerx_tables = sagerx_tables.set_axis(range(len(sagerx_tables)))
sagerx_tables


# In[ ]:





# In[153]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx'
table_name = 'dailymed_interaction'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
dailymed_interaction = pd.read_csv(path_csv_file, low_memory=False)
dailymed_interaction


# In[ ]:





# In[152]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx'
table_name = 'dailymed_organization_text'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
dailymed_organization_text = pd.read_csv(path_csv_file, low_memory=False)
dailymed_organization_text


# In[ ]:





# In[151]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx'
table_name = 'data_availability'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
data_availability = pd.read_csv(path_csv_file, low_memory=False)
data_availability


# In[ ]:





# In[150]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'dailymed_daily'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
dailymed_daily = pd.read_csv(path_csv_file, low_memory=False)
dailymed_daily


# In[ ]:





# In[149]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'dailymed_pharm_class'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
dailymed_pharm_class = pd.read_csv(path_csv_file, low_memory=False)
dailymed_pharm_class


# In[ ]:





# In[148]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'dailymed_rxnorm'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
dailymed_rxnorm = pd.read_csv(path_csv_file, low_memory=False)
dailymed_rxnorm


# In[ ]:





# In[147]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'dailymed_zip_file_metadata'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
dailymed_zip_file_metadata = pd.read_csv(path_csv_file, low_memory=False)
dailymed_zip_file_metadata


# In[ ]:





# In[146]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_enforcement'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_enforcement = pd.read_csv(path_csv_file, low_memory=False)
fda_enforcement


# In[ ]:





# In[145]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_excluded_package'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_excluded_package = pd.read_csv(path_csv_file, low_memory=False)
fda_excluded_package


# In[ ]:





# In[144]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_excluded_product'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_excluded_product = pd.read_csv(path_csv_file, low_memory=False)
fda_excluded_product


# In[ ]:





# In[143]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_ndc_package'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_ndc_package = pd.read_csv(path_csv_file, low_memory=False)
fda_ndc_package


# In[ ]:





# In[142]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_ndc_product'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_ndc_product = pd.read_csv(path_csv_file, low_memory=False)
fda_ndc_product


# In[ ]:





# In[141]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_unfinished_product'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_unfinished_product = pd.read_csv(path_csv_file, low_memory=False)
fda_unfinished_product


# In[ ]:





# In[140]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_unfinished_product'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_unfinished_product = pd.read_csv(path_csv_file, low_memory=False)
fda_unfinished_product


# In[ ]:





# In[139]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'fda_unii'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
fda_unii = pd.read_csv(path_csv_file, low_memory=False)
fda_unii


# In[ ]:





# In[138]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'nadac'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
nadac = pd.read_csv(path_csv_file, low_memory=False)
nadac


# In[ ]:





# In[137]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'orange_book_exlusivity'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
orange_book_exlusivity = pd.read_csv(path_csv_file, low_memory=False)
orange_book_exlusivity


# In[ ]:





# In[136]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'orange_book_patent'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
orange_book_patent = pd.read_csv(path_csv_file, low_memory=False)
orange_book_patent


# In[ ]:





# In[135]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'orange_book_products'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
orange_book_products = pd.read_csv(path_csv_file, low_memory=False)
orange_book_products


# In[ ]:





# In[134]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'purple_book'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
purple_book = pd.read_csv(path_csv_file, low_memory=False)
purple_book


# ## rxclass_atc_to_product

# In[108]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxclass_atc_to_product'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
rxclass_atc_to_product = pd.read_csv(path_csv_file, low_memory=False)
rxclass_atc_to_product


# ## rxnorm_historical

# In[107]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxnorm_historical'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
rxnorm_historical = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_historical


# ## rxnorm_rxnatomarchive

# In[106]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxnorm_rxnatomarchive'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
rxnorm_rxnatomarchive = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxnatomarchive


# ## rxnorm_rxnconso

# In[105]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxnorm_rxnconso'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
rxnorm_rxnconso = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxnconso


# ## rxnorm_rxncui

# In[103]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxnorm_rxncui'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
rxnorm_rxncui = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxncui


# ## rxnorm_rxncuichanges

# In[102]:


# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxnorm_rxncuichanges'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
# view dataframe
import pandas as pd
rxnorm_rxncuichanges = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxncuichanges


# In[100]:


import os
# table_name = str(input("Enter table name: "))

schema = 'sagerx_lake'
table_name = 'rxnorm_rxncuichanges'
csv_file_name = table_name + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
if os.path.isfile(path_csv_file) == True:
    print(f'{table_name} exist')
else:
    host_ip = '192.168.48.129'
    # host_ip = '192.168.48.132'
    import psycopg2
    conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                            port = '5432', user = 'sagerx', password = 'sagerx')
    curs = conn.cursor()
    fid = open(path_csv_file, 'w', encoding="utf-8")
    query = f"SELECT * FROM {schema}.{table_name}"
    sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
    curs.copy_expert(sql, fid)
    fid.close()
# view dataframe
if os.path.isfile(path_csv_file) == True:
    import pandas as pd
    rxnorm_rxncuichanges = pd.read_csv(path_csv_file, low_memory=False)
    rxnorm_rxncuichanges
else:
    print(f'{table_name} not exist')


# ## rxnorm_rxndoc

# In[94]:


host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()

# table_name = str(input("Enter table name: "))
schema = 'sagerx_lake'
table_name = 'rxnorm_rxndoc'
schema_table = schema + '.' + table_name
csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w', encoding="utf-8")
query = f"SELECT * FROM {schema}.{table_name}"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
rxnorm_rxndoc = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxndoc


# ## dailymed_daily

# In[81]:


host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()

# table_name = str(input("Enter table name: "))
table_name = 'sagerx_lake.dailymed_daily'
csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w', encoding="utf-8")
query = "SELECT * FROM sagerx_lake.dailymed_daily"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
dailymed_daily = pd.read_csv(path_csv_file, low_memory=False)
dailymed_daily


# ## sagerx_lake.orange_book_products

# In[80]:


host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()

# table_name = str(input("Enter table name: "))
table_name = 'sagerx_lake.orange_book_products'
csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w', encoding="utf-8")
query = "SELECT * FROM sagerx_lake.orange_book_products"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
orange_book_products = pd.read_csv(path_csv_file, low_memory=False)
orange_book_products


# ## sagerx_lake.rxnorm_rxnrel

# In[79]:


host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()

table_name = str(input("Enter table name: "))
csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w', encoding="utf-8")
query = "SELECT * FROM sagerx_lake.rxnorm_rxnrel"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
rxnorm_rxnrel = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxnrel


# In[77]:


host_ip = '192.168.48.129'
# host_ip = '192.168.48.132'
import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host_ip, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()


# ## Extract sagerx_lake.rxterms_ingredients

# In[6]:


fid = open('../sagerxdata/rxterms_ingredients.csv', 'w')


# In[7]:


sql = "COPY (SELECT * FROM sagerx_lake.rxterms_ingredients) TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()


# In[9]:


import pandas as pd
rxterms_ingredients = pd.read_csv('../sagerxdata/rxterms_ingredients.csv')
rxterms_ingredients


# ## sagerx_lake.rxterms

# In[10]:


table_name = str(input("Enter table name: "))


# In[47]:


csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w')
sql = "COPY (SELECT * FROM sagerx_lake.rxterms) TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
rxterms = pd.read_csv(path_csv_file)
rxterms


# ## sagerx_lake.rxnorm_rxnsty

# In[48]:


table_name = str(input("Enter table name: "))


# In[49]:


csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w')


# In[53]:


sql = "COPY (SELECT * FROM sagerx_lake.rxnorm_rxnsty) TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
rxnorm_rxnsty = pd.read_csv(path_csv_file)
rxnorm_rxnsty


# ## sagerx_lake.rxnorm_rxnsat

# In[66]:


table_name = str(input("Enter table name: "))


# In[78]:


table_name = str(input("Enter table name: "))
csv_file_name = table_name.replace('sagerx_lake.', '') + '.csv'
path_csv_file = '../sagerxdata/' + csv_file_name
fid = open(path_csv_file, 'w', encoding="utf-8")
query = "SELECT * FROM sagerx_lake.rxnorm_rxnsat"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
rxnorm_rxnsat = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxnsat


# In[ ]:





# In[2]:


import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = '192.168.48.129', 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()

# export to csv
fid = open('../sagerxdata/dailymed_rxnorm_filtered.csv', 'w')
sql = "COPY (SELECT * FROM sagerx_lake.dailymed_rxnorm WHERE rxstr LIKE '%liquid soap%' OR rxstr LIKE '%Topical Solution%' OR rxstr LIKE '%Facial Scrub%') TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()


# In[3]:





# ### chemas sagerx
                  List of relations
 Schema |            Name            | Type  | Owner  
--------+----------------------------+-------+--------
 sagerx | dailymed_interaction       | table | sagerx
 sagerx | dailymed_organization_text | table | sagerx
 sagerx | data_availability          | table | sagerx
 sagerx | pg_stat_statements         | view  | sagerx
 sagerx | pg_stat_statements_info    | view  | sagerx
# ### chemas sagerxdev

# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


dailymed_rxnorm_filtered = pd.read_csv('../sagerxdata/dailymed_rxnorm_filtered.csv')
dailymed_rxnorm_filtered.head()


# In[3]:


import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()


# In[ ]:





# In[ ]:





# In[ ]:





# ## sagerx_dev.int_mthspl_products_to_inactive_ingredients

# In[ ]:


import psycopg2
conn = psycopg2.connect(dbname='sagerx', host = host, 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()


# drug_input = str(input("Enter name: "))
drug_name = str(input("Enter name: "))
# drug_name = drug_input.lower().replace(' ', '+').replace('-','+')

# Save file inactive_ingredient_list.txt
import os
print(drug_name)
drug_name_iig_file = drug_name + "_inactive_ingredient_list.csv"
drug_name_iig_file_path = os.path.join('sagerxdata', drug_name_iig_file)

query = "SELECT * FROM sagerx_dev.int_mthspl_products_to_inactive_ingredients WHERE product_name LIKE '%" + drug_name + "%'" 
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


# In[ ]:





# In[ ]:




