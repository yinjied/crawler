import pymysql
import datetime
host="139.198.19.54"
user = "crawler"
passwd = "crawler"
dbname = "test"

def create_table(table_name):
    db = pymysql.connect(host,user,passwd,dbname,charset='utf8')
    cursor = db.cursor()
    sql = """CREATE TABLE %s(
             ID INT   AUTO_INCREMENT,
             a  varCHAR(100) NOT NULL,
             b  varCHAR(200) not null,
             PRIMARY KEY (ID))"""%table_name
    cursor.execute(sql)
    db.close()

def insert_table(table_name,date):
    db = pymysql.connect(host,user,passwd,dbname,charset='utf8')
    cursor = db.cursor()
    #sql = "INSERT INTO %s"%table_name  + "(district, district_url) VALUES (%s, %s)"%(data, data)
    #sql = "INSERT INTO %s (district, %s,district_url) VALUES (%s, %s)"%(table_name,table_name, data, data)
    sql = "INSERT INTO %s"%table_name  + "(a, b, c) VALUES (%s, %s, %s)"
    cursor.execute(sql,(date, date, date))
    db.commit()
    db.close()
def update_table(table_name,date):
    db = pymysql.connect(host,user,passwd,dbname,charset='utf8')
    cursor = db.cursor()
    sql = "update  %s"%table_name + " set create_date = %s"
    print(sql)
    cursor.execute(sql,date)
    db.commit()
    db.close()
#print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#today = datetime.datetime.yesterday().strftime('%Y-%m-%d')
#create_table('ab')
today = '2018-11-27'
print(today)
print(type(today))
table_name = 'apartment'
update_table(table_name, today)
