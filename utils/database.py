import pymysql
import time


def get_conn():
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='987654321.',
                           db='refinement')
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    close_conn(conn, cursor)
    return result


def get_raw_data():
    return (('请提高安全性。')) #, ('服务等级降低'), ('1234.5将保密性和优先级提高2级，'))


"""
查询预置命令数据库
输入：一个字符串
输出：一个字符串或者None（表示该输入字符串对应的预置命令，或无对应命令则返回None）
"""
def get_order_data():

    return 1


"""
保存精化结果
输入：一个需求和一个命令
输出：一个boolean值（保存成功为0，出现异常为1）
"""
def save_refined_data(demand, order):

    return 1


"""
取服务器信息，以供前端可视化
输入：无
输出：最新一批数据（主键update_time最大）
"""
def get_refined_data():
    sql = 'select update_time,' \
          'frontend, ' \
          'backend1, ' \
          'backend2, ' \
          'reject ' \
          'from servers ' \
          'order by update_time desc limit 15'
    result = query(sql)
    return result


if __name__ == '__main__':
    result = get_refined_data()