
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2019/11/8
# @Author: Tigerots

from flask import Flask, request, jsonify, redirect, url_for
from  werkzeug.routing import BaseConverter


# 新建一个Flask可运行实体
app = Flask(__name__)

# 配置对象, 定义一系列给app的参数
class Config(object):
    DEBUG = True

# 正则匹配路由
class Regex1(BaseConverter):
    def __init__(self, url_map, *args):
        super(Regex1, self).__init__(url_map)
        super().__init__(map)
        self.regex = args[0]
# 用正则是防爬虫
app.url_map.converters['re'] = Regex1
@app.route('/user/<re("[a-z]{3}"):user_id>')
def user_info(user_id):
    return "user_id:{}".format(user_id)

# 加载配置
app.config.from_object(Config)

# 装饰器: 在运行实体上绑定URL路由,将路由映射到视图函数
# 路由可以传递参数
@app.route('/user/<string:user_id>', methods=['GET','POST'])
def myapp(user_id):
    # return 返回给浏览器
    print(user_id)
    return "=====Hello World!====="+request.method

# 视图常用逻辑
@app.route('/index')
def index():
    json_dict = \
    {
        "user_id":10,
        "user_name":"Tigerots"
    }
    return jsonify(json_dict)
# 重定向
@app.route("/demo1")
def demo1():
    return redirect(url_for("index"))

# 重定向
@app.route("/demo2")
def demo2():
    return redirect("http://www.baidu.com")

# 自定义状态
@app.route("/demo3")
def demo3():
    return "Test",1288




if __name__ == '__main__':
    app.run()
