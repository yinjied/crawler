import pymysql
host="139.198.19.54"
user = "crawler"
passwd = "crawler"
dbname = "test"


def func():
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
    cursor = conn.cursor()

    sql = "SELECT distinct xiaoqu_name, xiaoqu_url FROM apartment"
    cursor.execute(sql)
    xiaoqu_tuple = cursor.fetchall()
    for item in xiaoqu_tuple:
        sql = "insert into xiaoqu (xiaoqu_name, xiaoqu_url) values (%s, %s)"
        cursor.execute(sql,item)
    conn.commit()
    conn.close()

func()
