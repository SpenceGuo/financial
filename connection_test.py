import pymysql

host = "127.0.0.1:3306"
port = "3306"
username = "root"
password = ""
dbname = "financial"

# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "financial")

# SQL 插入语句
sql = 'select * from original_max_min'
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print(data)

# 关闭数据库连接
db.close()
