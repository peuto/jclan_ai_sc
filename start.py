# coding=utf-8
from flask import Flask, request
from flask_cors import *
from sqlalchemy.orm.exc import NoResultFound

from DBManager import *
from entities import *
from utils import *

app = Flask(__name__)
# 解决跨域问题：No 'Access-Control-Allow-Origin' header is present on the requested resource.
CORS(app, supports_credentials=True)
# 解决中文显示的问题
app.config['JSON_AS_ASCII'] = False


db_mananager = DBManager("mysql+mysqlconnector", "mysql57.rdsmlq1es7zb7bt.rds.gz.baidubce.com:3306","rdsroot","jclan@2019", "JClan_AI")
if db_mananager != None:
    print("DB is OK!")


@app.route('/')
def hello_world():
    return '<h3>JClan AI Edu</h3>'

# 根据ID获取用户
@app.route('/get_user_by_id', methods=['POST', 'GET'])
def get_user_by_id():
    p_uid = request.values.get("id")
    db_session = db_mananager.create_session()
    try:
        user = db_session.query(User).filter(User.id == p_uid).one()
        msg = Message("获取到一个用户", 1)
        str_json = user.to_json(msg)
    except NoResultFound:
        msg = Message("未找到用户", 0)
        str_json = json.dumps(msg.__dict__, ensure_ascii=False)
    db_session.close()
    return str_json

# 创建新用户
@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    p_name = request.values.get("name")
    p_mobile = request.values.get("mobile")
    p_gender = request.values.get("gender")
    p_open_id = request.values.get("open_id")
    print(p_name, p_mobile, p_gender, p_open_id)

    db_session = db_mananager.create_session()
    user_exist = db_session.query(User).filter(User.open_id == p_open_id).one()
    if user_exist is not None:
        user = User(name=p_name, mobile=p_mobile, gender=str_to_bool(p_gender), open_id=p_open_id)
        db_session.add(user)
        db_session.commit()
        user_new = db_session.query(User).filter(User.open_id == p_open_id).one()
        msg = Message("创建用户成功", 1)
        str_json = user_new.to_json(msg)
    else:
        msg = Message("用户已存在", 2)
        str_json = user_exist.to_json(msg)

    db_session.close()

    return str_json


if __name__ == '__main__':
    app.run(debug=True)
