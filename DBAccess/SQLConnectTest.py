#-*- coding utf-8 -*-

import pyodbc

def main():
    connectString = "DRIVER={SQL SERVER}; SERVER=(local)\SQLEXPRESS;DATABASE="";TrustedConnction=yes;"
    sql = "select sysdb.name from sysdatabases sysdb"
   

    conn = pyodbc.connect(connectString)

    cursor = conn.cursor()
    cursor.execute(sql)

    for row in cursor:
        print(row)

    conn.close()

if __name__ =="__main__":
    main()
