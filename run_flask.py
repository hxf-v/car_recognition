# coding=utf8
from sql_serach import MSSQL
from flask import Flask, jsonify
from flask import request
import json
from flask_cors import CORS

# 连接数据库
ms = MSSQL(host='172.16.254.196',
           user='sa',
           pwd='ahu123',
           db='VMWare', )

app = Flask(__name__)


@app.route('/send_json', methods=['GET', 'POST'])
def send_json():
    """
    根据post方法获取用户名、密码
    :return:
    """
    if request.method == 'POST':
        data_json = request.get_json()  # 获取postman传来的json数据
        user_id = data_json["sfzh"]  # 获取用户id
        res_list = ms.ExecQuery("SELECT * FROM ahu_Teacher WHERE sfzh='%s' " % user_id)  # 获取数据库中用户名和密码,查询用户是否在表内

        res_na = []  # 定义空list 存放返回的用户姓名和用户院系
        for tuple_name in res_list:
            for str_name in tuple_name:
                if str_name is not None:
                    str_name.strip()
                    res_na.append(str_name.strip())
                    # print(str_name)
        # res_dict = {"name": res_na[1], "xueyuan": res_na[2]}

        name = res_na[1]
        words = res_na[2]
        return jsonify({'name': name, 'word': words})


# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     """
#     根据post方法获取用户名、密码
#     :return:
#     """
#     if request.method == 'GET':
#         return 'helloword'


print('backend post')  # 监测后端是否正确启动。
if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', threaded=True, debug=True, port=8081)
    CORS(app, supports_credentials=True)
