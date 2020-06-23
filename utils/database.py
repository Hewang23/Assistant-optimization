import pymysql


def get_conn():
    conn = pymysql.connect(host='',
                           user='',
                           password='',
                           db='')
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


def get_raw_date():
    # 暂时不用
    return 1


"""
查询助词数据库函数
输入：一个字符串
输出：一个boolean值（表示该字符串是否存在于助词库中）
"""
def get_zhuci_data():

    return 1


"""
查询预置命令数据库
输入：一个字符串
输出：一个字符串或者null（表示该输入字符串对应的预置命令，或无对应命令则返回null）
"""
def get_order_data():

    return 1


"""
保存精化结果
输入：一个命令
输出：一个boolean值（保存成功为0，出现异常为1）
"""
def save_refined_data():

    return 1


"""
取最终结果，以供前端可视化
输入：无
输出：最新一批处理过的数据（主键update_time最大）
"""
def get_refined_data():

    return 1