import db_config
import pymysql

host = db_config.host
port = db_config.port
username = db_config.username
password = db_config.password
dbname = db_config.dbname

filepath = ''

data = []

sql = 'SELECT datetime,openpx,lastpx,lowpx,highpx FROM his_cff WHERE securityid=\'IC0001\' ORDER BY datetime DESC'

db = pymysql.connect(host, username, password, dbname)
cursor = db.cursor()
cursor.execute(sql)

result = cursor.fetchall()

for row in result:
    onedata = []

    datetime = row[0]
    openpx = row[1]
    lastpx = row[2]
    lowpx = row[3]
    highpx = row[4]

    onedata.append(datetime)
    onedata.append(openpx)
    onedata.append(lastpx)
    onedata.append(lowpx)
    onedata.append(highpx)

    data.append(onedata)

print(data)
