import pymysql
import pymongo
import json

host = '127.0.0.1'
port = '3306'
username = 'root'
password = ''
dbname = 'financial'
tbname = 'data'

data_json = []

db = pymysql.connect(host, username, password, dbname)
sql = 'SELECT * FROM ' + tbname
cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
    onedata = []
    datetime = row[0]
    value = row[1]
    onedata.append(datetime)
    onedata.append(value)
    data_json.append(onedata)

print(data_json)

