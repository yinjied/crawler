import pymysql
host="192.168.183.130"
user = "crawler"
passwd = "crawler"
dbname = "test"

db = pymysql.connect(host,user,passwd,dbname )
cursor = db.cursor()

sql = "INSERT INTO district (district, district_url) VALUES (%s, %s)"
sql = "SELECT * FROM district"
cursor.execute(sql)
ret = cursor.fetchone()
ret1 = cursor.fetchone()
print(type(ret))
print(ret)
print(ret1)
db.close()
print('你好')
