import pymysql

host = "localhost"
port = "3306"
username = "root"
password = ""
dbname = "financial"

path = ''
security_ids = [600000,
               600016,
               600019,
               600028,
               600029,
               600030,
               600036,
               600048,
               600050,
               600104,
               600111,
               600267,
               600309,
               600340,
               600519,
               600547,
               600585,
               600606,
               600690,
               600703,
               600887,
               600958,
               600999,
               601006,
               601088,
               601166,
               601169,
               601186,
               601211,
               601229,
               601288,
               601318,
               601328,
               601336,
               601360,
               601390,
               601398,
               601601,
               601628,
               601668,
               601688,
               601766,
               601800,
               601818,
               601857,
               601878,
               601881,
               601988,
               601989,
               603993
               ]
path_title = r'C:/Users/TangGuo/Desktop/finance/max_min/'
db = pymysql.connect(host, username, password, dbname)
cursor = db.cursor()

for i in range(50):
    image_path = path_title + str(security_ids[i]) + '.csv.png'
    csvmax_path = path_title + str(security_ids[i]) + '.csvmax.csv'
    csvmin_path = path_title + str(security_ids[i]) + '.csvmin.csv'
    sql = 'INSERT INTO original_max_min(securityid, image_path, csvmax_path, csvmin_path) VALUES(' + str(
        security_ids[i]) + \
          ',' + '\'' + image_path + '\',' + '\'' + csvmax_path + '\'' + ',\'' + csvmin_path + '\')'
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

db.close()
