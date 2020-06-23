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
def update_info():
    data = utils.database.get_refined_data()
    return 1


# 页面左下角功能待定
@app.route('/left-bottom')
def update_lb():
    return 1


# 后端主循环待定
@app.route('/backend_loop')
def backend():
    subject, data = utils.database.get_raw_date()
    orders = utils.nlp.process(data)
    # merge....
    return 1


if __name__ == '__main__':
    app.run()
