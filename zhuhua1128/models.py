#-*-coding:utf-8-*-

from exts import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	email = db.Column(db.String(50),nullable=True)
	username = db.Column(db.String(50),nullable=True)
	password = db.Column(db.String(10),nullable=True)
	level = db.Column(db.String(50), nullable=True)
	DDC_ID = db.Column(db.String(50), nullable=True)

class Ddc_data(db.Model):
	__tablename__ = 'DDC_data'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	begintime = db.Column(db.DateTime, nullable=True)
	DDC_ID = db.Column(db.String(50), nullable=True)
	biaohao= db.Column(db.String(50), nullable=True)
	data = db.Column(db.String(50), nullable=True)
	consumption = db.Column(db.String(50), nullable=True)
	endtime = db.Column(db.DateTime, nullable=True)
	cmd1 = db.Column(db.String(50), nullable=True)
	cmd2 = db.Column(db.String(50), nullable=True)
	cmdall1 = db.Column(db.String(50), nullable=True)
	cmdall2 = db.Column(db.String(50), nullable=True)

class Ddc_refresh(db.Model):
	__tablename__ = 'DDC_refresh'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	DDC_ID = db.Column(db.String(50), nullable=True)
	biaohao= db.Column(db.String(50), nullable=True)
	data = db.Column(db.String(50), nullable=True)
	endtime = db.Column(db.DateTime, nullable=True)
	consumption = db.Column(db.String(50), nullable=True)

class Ddc_info(db.Model):
	__tablename__ = 'DDC_info'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	DDC_ID = db.Column(db.String(50), nullable=True)
	address = db.Column(db.String(50), nullable=True)
	number = db.Column(db.String(50), nullable=True)
	type = db.Column(db.String(50), nullable=True)
	biaohao = db.Column(db.String(50), nullable=True)
	flag1 = db.Column(db.String(50), nullable=True)
	flag2 = db.Column(db.String(50), nullable=True)
	endtime = db.Column(db.DateTime, nullable=True)

class Ddc_state(db.Model):
	__tablename__ = 'DDC_state'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	DDC_ID = db.Column(db.String(50), nullable=True)
	state = db.Column(db.String(50), nullable=True)
	zhuangtaizi = db.Column(db.String(50), nullable=True)
	mark1 = db.Column(db.String(50), nullable=True)
	mark2 = db.Column(db.String(50), nullable=True)
	sign = db.Column(db.String(50), nullable=True)
	endtime = db.Column(db.DateTime, nullable=True)




