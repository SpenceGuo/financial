import pymysql
import pymongo
import json

servername = "202.120.36.28:23306"
port = "23306"
username = "qi"
password = "password"
dbname = "SH_Stock_Exchange"
jsonfile_savepath = 'D:/GithubProjects/financial/json/IC0001.json'
stock_id = 'IC0001.json'

stock_json = []

str_c = '\''
sql = 'SELECT datetime,preclosepx,openpx,highpx,lowpx,lastpx FROM his_cff WHERE securityid=\'IC0001\' ORDER BY datetime DESC'

db = pymysql.connect(servername, username, password, dbname)
cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()
for row in data:
    onedata = {}

    datetime = row[0]
    preclosepx = row[1]
    openpx = row[2]
    highpx = row[3]
    lowpx = row[4]
    lastpx = row[5]

    onedata['datetime'] = datetime
    onedata['preclosepx'] = preclosepx
    onedata['openpx'] = openpx
    onedata['highpx'] = highpx
    onedata['lowpx'] = lowpx
    onedata['lastpx'] = lastpx
    stock_json.append(onedata)

    print("JSON 对象：", json.dumps(stock_json))
    # print(datetime, preclosepx, openpx, highpx, lowpx, lastpx, end='\n')
db.close()

# f = open(jsonfile_savepath, 'w')
# f.write(json.dumps(stock_json))
# f.close()
