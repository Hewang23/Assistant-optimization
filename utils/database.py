from utils import database
from utils import time
from utils import nlp
import traceback
import pymysql

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
def get_order_data(word):
    cursor = None
    conn = None
    req = []
    try:
        conn, cursor = get_conn()
        sql = "SELECT action FROM instruction WHERE struction = %s"
        cursor.execute(sql, word)
        res = cursor.fetchall()
        for i in range(len(res)):
            req.append(res[i][0])
        print("操作执行成功")
        return req[0]
    except:
        # traceback.print_exc()
        print("操作执行失败")
        return None
    finally:
        close_conn(conn, cursor)


"""
保存精化结果
输入：一个需求和一个命令
输出：一个boolean值（保存成功为0，出现异常为1）
"""
def save_refined_data(tim, demand, order):
    cursor = None
    conn = None
    # tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    conn, cursor = get_conn()
    sql = "insert into log(log_time, demand_log, order_log) values(%s, %s, %s)"
    cursor.execute(sql, [tim, demand, order])
    conn.commit()
    print("操作日志保存成功")
    close_conn(conn, cursor)

    # 创建日志表
    # SQL = """CREATE TABLE `log` (
    #   `log_time` varchar(255) NOT NULL,
    #   `demand_log` varchar(255) DEFAULT NULL,
    #   `order_log` varchar(255) DEFAULT NULL,
    #   PRIMARY KEY (`log_time`)
    # ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    # """


"""
取服务器信息，以供前端可视化
输入：无
输出：最新一批数据（主键update_time最大）
"""
def get_server_data():
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
    sentence = '1234.5将保密性和优先级提高2级，'
    tim = time.get_time()
    order = nlp.process(sentence)
    database.save_refined_data(tim, sentence, order)
    # merge....
    # return jsonify({'demand': sentence, 'order': order})