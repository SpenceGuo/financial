import db_config
import pymysql

class Stock:
    host = db_config.host
    port = db_config.port
    username = db_config.username
    password = db_config.password
    dbname = db_config.dbname

    def getData(self, securityid):
        data = []
        sql = 'SELECT datetime,openpx,lastpx,lowpx,highpx FROM his_cff WHERE securityid=\'' + securityid + '\'' + ' ORDER BY datetime ASC'

        db = pymysql.connect(self.host, self.username, self.password, self.dbname)
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

        return data



