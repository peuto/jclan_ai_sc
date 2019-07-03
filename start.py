# coding=utf-8
from flask import Flask, request
from flask_cors import *
from DBManager import *

import json

app = Flask(__name__)
# 解决跨域问题：No 'Access-Control-Allow-Origin' header is present on the requested resource.
CORS(app, supports_credentials=True)
# 解决中文显示的问题
app.config['JSON_AS_ASCII'] = False


db_mananager = DBManager("mysql+mysqlconnector","root","jclan@2019","mysql57.rdsmlq1es7zb7bt.rds.gz.baidubce.com", "JClan_AI")
if db_mananager != None:
    print("DB is OK!")


@app.route('/')
def hello_world():
    return '<h1>JClan AI Edu</h1>'


if __name__ == '__main__':
    app.run()
