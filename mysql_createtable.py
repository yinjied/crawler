import pymysql
host="localhost"
user = "crawler"
passwd = "crawler"
dbname = "test"
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
