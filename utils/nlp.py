from jieba.analyse import extract_tags
import utils

from utils import database

"""
将自然语言按词拆分
输入：一个句子
输出：不包含数字的词组成的list
"""
def divide_into_words(sentence):
    return extract_tags(sentence)


"""
匹配预置命令
输入：词组成的list
输出：一个list（输入的每个词都对应了0或1个命令）
"""
def match_orders(words):
    order = []
    for w in words:
        if not is_digit(w):
            result = database.get_order_data(w)
            if result:
                order.append(result)
    return order


"""
判断该字符串是否为数字
输入：一个字符串
输出：一个boolean值（是为Ture，不是为False）
"""
def is_digit(word):
    try:
        digit = float(word)
        result = True
    except:
        result = False
    return result


# 格式整理
def trim(words):
    return ', '.join(words)


# 主函数
def process(s):
    orders = []
    # for s in sentences:
    words = divide_into_words(s)
    order = trim(match_orders(words))
    # orders.append(order)
    print(order)
    return order


if __name__ == '__main__':
    process(s='1234.5将保密性和优先级提高2级，')