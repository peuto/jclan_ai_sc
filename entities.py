# coding = utf-8

from sqlalchemy import Column, String, create_engine, Boolean, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(32), nullable=False)
    mobile = Column(String(16), nullable=False)
    gender = Column(Boolean, nullable=False)
    open_id = Column(String(64), nullable=False)

    def to_json(self):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        print(dict)
        str_json = json.dumps(dict)
        return str_json