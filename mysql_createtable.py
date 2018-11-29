import pymysql
host="139.198.19.54"
user = "crawler"
passwd = "crawler"
dbname = "test"
'''
db = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
cursor = db.cursor()
sql = """CREATE TABLE xiaoquinfo (
         ID INT   AUTO_INCREMENT,
         xiaoqu_name  varCHAR(100) NOT NULL,
         xiaoqu_url  varCHAR(200) not null,
         build_time  varCHAR(200) not null,
         build_type  varCHAR(200) not null,
         pm_price  varCHAR(200) not null,
         pm_compnay  varCHAR(200) not null,
         build_company  varCHAR(200) not null,
         sum_buildings  varCHAR(200) not null,
         sum_apartments  varCHAR(200) not null,
         create_date  date not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect(host,user,passwd,dbname,charset='utf8' )
cursor = db.cursor()
sql = """CREATE TABLE xiaoqu (
         ID INT   AUTO_INCREMENT,
         xiaoqu_name  varCHAR(100) NOT NULL,
         xiaoqu_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()


db = pymysql.connect(host,user,passwd,dbname )
cursor = db.cursor()
sql = """CREATE TABLE district (
         ID INT   AUTO_INCREMENT,
         district  varCHAR(100) NOT NULL,
         district_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect(host,user,passwd,dbname )
cursor = db.cursor()
sql = """CREATE TABLE street (
         ID INT   AUTO_INCREMENT,
         district  varCHAR(100) NOT NULL,
         street varchar(100) not null,
         street_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect(host,user,passwd,dbname )
cursor = db.cursor()
sql = """CREATE TABLE page (
         ID INT   AUTO_INCREMENT,
         street  varCHAR(100) NOT NULL,
         page varchar(100) not null,
         page_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect(host,user,passwd,dbname )
cursor = db.cursor()
sql = """CREATE TABLE apartment (
         ID INT   AUTO_INCREMENT,
         street  varCHAR(100) NOT NULL,
         apartment varchar(200) not null,
         apartment_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()
'''
