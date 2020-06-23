from jieba.analyse import extract_tags
import database

"""
将自然语言按词拆分
输入：一个句子
输出：不包含数字的词组成的list
"""
def divide_into_words(sentence):
    return extract_tags(sentence)


"""
去除助词
输入：词组成的list
输出：不包含助词的词组成的list
"""
def remove_zhuci(words):
    return 1


"""
匹配预置命令
输入：词组成的list
输出：一个list（输入的每个词都对应了0或1个命令）
"""
def match_orders(words):
    return 1


# 格式整理
def trim(words):
    return 1


# 主函数
def process(sentences):
    orders = []
    for s in sentences:
        words = remove_zhuci(divide_into_words(s))
        for w in words:
            orders.append(trim(match_orders(w)))
    return sentences, orders


if __name__ == '__main__':
    print(database.get_raw_date())