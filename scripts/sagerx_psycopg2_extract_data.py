import sys
sys.path.append('..')
import psycopg2
host = '192.168.48.129'
conn = psycopg2.connect(dbname='sagerx', host = '192.168.48.129', 
                        port = '5432', user = 'sagerx', password = 'sagerx')
curs = conn.cursor()

# export to csv
fid = open('../sagerxdata/dailymed_rxnorm_filtered.csv', 'w')
sql = "COPY (SELECT * FROM sagerx_lake.dailymed_rxnorm WHERE rxstr LIKE '%liquid soap%' OR rxstr LIKE '%Topical Solution%' OR rxstr LIKE '%Facial Scrub%') TO STDOUT WITH CSV HEADER"
curs.copy_expert(sql, fid)
fid.close()

# SELECT * FROM sagerx_dev.int_mthspl_products_to_inactive_ingredients WHERE product_name LIKE '%tirzepatide%'