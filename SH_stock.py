import db_config
import pymysql

class Stock:
    __host = db_config.host
    __port = db_config.port
    __username = db_config.username
    __password = db_config.password
    __dbname = db_config.dbname

    def getData(self, securityid):
        data = []
        sql = 'SELECT datetime,openpx,lastpx,lowpx,highpx FROM his_cff WHERE securityid=\'' + securityid + '\'' + ' ORDER BY datetime ASC'

        db = pymysql.connect(self.__host, self.__username, self.__password, self.__dbname)
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

    def getDate(self, securityid):
        data = []
        sql = 'SELECT datetime FROM his_cff WHERE securityid=\'' + securityid + '\'' + ' ORDER BY datetime ASC'

        db = pymysql.connect(self.__host, self.__username, self.__password, self.__dbname)
        cursor = db.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        for row in result:

            datetime = row[0]

            data.append(datetime)

        return data

    def getOData(self, securityid):
        data = []
        sql = 'SELECT openpx,lastpx,lowpx,highpx FROM his_cff WHERE securityid=\'' + securityid + '\'' + ' ORDER BY datetime ASC'

        db = pymysql.connect(self.__host, self.__username, self.__password, self.__dbname)
        cursor = db.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        for row in result:
            onedata = []

            openpx = row[0]
            lastpx = row[1]
            lowpx = row[2]
            highpx = row[3]

            onedata.append(openpx)
            onedata.append(lastpx)
            onedata.append(lowpx)
            onedata.append(highpx)

            data.append(onedata)

        return data

