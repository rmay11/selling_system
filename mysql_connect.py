import pymysql
import sys
host = 'localhost'
user = 'root'
password = '123456'
database = 'test'


try:
    conn = pymysql.connect(host=host,user=user,password=password,database=database)

    #print("数据库连接成功\n")
except Exception as err:
    print("数据库连接失败")
    sys.exit(0)
cursor = conn.cursor()
