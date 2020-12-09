
import pymysql

def DBconnection():
    mysqlcon = pymysql.connect(host='localhost',
                                user='root',
                                password='#357A$de2#w',
                                db='doctorapi',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)


    return mysqlcon



 
