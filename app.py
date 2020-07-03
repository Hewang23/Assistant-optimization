from flask import Flask
from flask import jsonify
from datetime import timedelta
from flask import render_template
from utils.database import get_refined_data
from utils.time import get_time

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)


@app.route('/')
def start():
    return render_template('main.html')


@app.route('/time')
def update_time():
    return get_time()

#
# @app.route('/info')
# def update_info():
#     # sentence = utils.database.get_raw_data()
#     order = utils.nlp.process(sentence)
#     utils.database.save_refined_data(sentence, order)
#     # merge....
#     return jsonify({'demand': sentence, 'order': order})


# 页面左下角功能待定
# 目前暂时决定为模拟的实时服务器参数，实现在utils.sim_server中
@app.route('/left-bottom')
def update_lb():
    result = get_refined_data()
    time_list = []
    frontend = []
    backend1 = []
    backend2 = []
    reject = []
    for t, f, b1, b2, r in result[::-1]:
        time_list.append(str(t)[11:])
        frontend.append(f)
        backend1.append(b1)
        backend2.append(b2)
        reject.append(r)
    return jsonify({'time': time_list,
                    'frontend': frontend,
                    'backend1': backend1,
                    'backend2': backend2,
                    'reject': reject})


if __name__ == '__main__':
    app.run()
