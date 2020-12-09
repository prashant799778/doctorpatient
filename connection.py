
import pymysql

def DBconnection():
    mysqlcon = pymysql.connect(host='localhost',
                                user='root',
                                password='s35JqVTs#t-RYs4$',
                                db='doctorapi',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)


    return mysqlcon



 
