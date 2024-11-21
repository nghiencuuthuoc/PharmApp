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
query = "SELECT * FROM sagerx_lake.rxnorm_rxnsat"
sql = "COPY (" + query + ") TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()
import pandas as pd
rxnorm_rxnsat = pd.read_csv(path_csv_file, low_memory=False)
rxnorm_rxnsat