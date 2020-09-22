import datetime
from datetime import date

import requests
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    stu_id = request.args.get('id', '')
    today = date.today()

    full_html = ""
    for i in range(7):
        d1 = today.strftime("%Y-%m-%d")
        url = f"http://219.216.96.73/pyxx/App_Ajax/GetkcHandler.ashx?kcdate={d1}&xh={stu_id}"

        weekday = today.weekday() +1

        head = f"<h3>{d1}  星期{weekday}</h3>"
        full_html += head + requests.get(url).text
        today += datetime.timedelta(days=1)


    return full_html


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, debug=False, port=5000)
