
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2019/11/8
# @Author: Tigerots

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '=====Hello World!====='


if __name__ == '__main__':
    app.run()


