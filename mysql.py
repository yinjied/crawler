import pymysql
db = pymysql.connect("192.168.70.131","crawler","crawler","test" )
cursor = db.cursor()
sql = """CREATE TABLE district (
         ID INT   AUTO_INCREMENT,
         district  varCHAR(20) NOT NULL,
         district_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect("192.168.70.131","crawler","crawler","test" )
cursor = db.cursor()
sql = """CREATE TABLE street (
         ID INT   AUTO_INCREMENT,
         district  varCHAR(20) NOT NULL,
         street varchar(40) not null,
         street_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect("192.168.70.131","crawler","crawler","test" )
cursor = db.cursor()
sql = """CREATE TABLE page (
         ID INT   AUTO_INCREMENT,
         street  varCHAR(20) NOT NULL,
         page varchar(40) not null,
         page_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()

db = pymysql.connect("192.168.70.131","crawler","crawler","test" )
cursor = db.cursor()
sql = """CREATE TABLE apartment (
         ID INT   AUTO_INCREMENT,
         street  varCHAR(20) NOT NULL,
         apartment varchar(200) not null,
         apartment_url  varCHAR(200) not null,
         PRIMARY KEY (ID))"""
cursor.execute(sql)
db.close()
