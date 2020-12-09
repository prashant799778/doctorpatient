
import pymysql

def DBconnection():
    mysqlcon = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='doctorapi',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)


    return mysqlcon



 
