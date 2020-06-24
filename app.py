from flask import Flask
from flask import jsonify
from datetime import timedelta
from flask import render_template
import utils

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)


@app.route('/')
def start():
    return render_template('main.html')


@app.route('/time')
def update_time():
    return utils.time.get_time()


@app.route('/info')
def up_date_info():
    sentence = utils.database.get_raw_data()
    order = utils.nlp.process(sentence)
    utils.database.save_refined_data(sentence, order)
    # merge....
    return jsonify({'demand': sentence, 'order': order})


# 页面左下角功能待定
# 目前暂时决定为模拟的实时服务器参数，实现在utils.sim_server中
@app.route('/left-bottom')
def update_lb():
    return 1


if __name__ == '__main__':
    app.run()
