import datetime

from zdppy_orm import *
import logging

# 创建日志对象
logger = logging.getLogger("zdppy_orm")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# 创建数据库连接
db = MySQLDatabase('zdppy_orm', host='127.0.0.1', user='root', passwd='root')


class BaseModel(Model):
   class Meta:
       database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类


class User(BaseModel):
   username = TextField()

   class Meta:
       table_name = 'user'


class Tweet(BaseModel):
   content = TextField()
   timestamp = DateTimeField(default=datetime.datetime.now)
   user = ForeignKeyField(User, backref="tweets")

   class Meta:
       table_name = 'tweet'


class Favorite(BaseModel):
   user = ForeignKeyField(User, backref="favorites")
   tweet = ForeignKeyField(Tweet, backref="favorites")


if __name__ == "__main__":
   db.connect()
   db.create_tables([User, Tweet, Favorite])