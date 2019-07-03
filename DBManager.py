# coding=utf-8

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

pymysql.install_as_MySQLdb()


class DBManager:

    # engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
    def __init__(self, db, host, usr, pwd, db_name):
        self.engine = create_engine(db+'://'+usr+':'+pwd+'@'+host+'/'+db_name)

    def create_session(self):
        # 创建DBSession类型
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        return session