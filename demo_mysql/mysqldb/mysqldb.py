from mysql.connector import pooling
import sys

__all__ = ["pool"]  # 暴露当前模块接口，排除不需要的sys,也可以控制*类似的导入


class Settings:
    config = dict(host="localhost", port="3306", user="root", password="103253201", database="demo", )


class MysqlPool(pooling.MySQLConnectionPool):

    def __init__(self, pool_size=5, config=None):
        if not config:
            config = Settings.config
        super(MysqlPool, self).__init__(pool_size=pool_size, **config)


try:
    pool = MysqlPool()
    print(pool.pool_name, pool.pool_size, pool.reset_session)
except Exception as e:
    print(e, )

if __name__ == '__main__':
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        cursor.execute("show databases")  # 查看库
        results = cursor.fetchall()
        for database in results:
            print(database, end="\n")
    except Exception as e:
        print(e)
    finally:
        if "con" in dir():
            con.close()  # 关闭连接即游
            print("关闭成功")
