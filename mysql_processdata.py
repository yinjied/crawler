import pymysql
host="localhost"
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


def insert_district(district_dict):
    if (len(district_dict) == 0):
        return 1
    conn = pymysql.connect(host,user,passwd,dbname )
    cursor = conn.cursor()
    for item in district_dict:
        sql = "INSERT INTO district (district, district_url) VALUES (%s, %s)"
        cursor.execute(sql, (item, district_dict[item]))
    conn.commit()
    conn.close()
    return 0
