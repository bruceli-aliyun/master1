from mysqldb.connection import MysqlPool


def executive():
    cursor.execute("show databases")  # 查看库
    results = cursor.fetchall()
    for database in results:
        print(database, end="\n")


try:
    pool = MysqlPool()
    con = pool.get_connection()
    cursor = con.cursor()
except Exception as e:
    print(e)
else:
    executive()
finally:
    if "con" in dir():
        con.close()  # 关闭连接即游标
