#encoding:utf-8

from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import *
from sqlalchemy import and_

import config
from decorators import login_required
from exts import db
from models import User, Ddc_data, Ddc_info, Ddc_state, Ddc_refresh

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
	return render_template('over_looking.html')

@app.route('/over_looking/')
def over_looking():
	return render_template('over_looking.html')

@app.route('/building_11/',methods=['GET','POST'])
@login_required
def building_11():
	alldata0 = Ddc_data.query.order_by('-endtime').all()
	context = {
		'alldata': alldata0[0:16],
		'data_page' : (len(alldata0) / 16) + 1,
		'data_state_1': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[7],
		'data_state_2': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[5],
		'data_state_3': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[6],
		'data_state_4': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[4],
		'data_state_5': Ddc_refresh.query.filter(Ddc_refresh.id == '1').first().data,
		'data_state_6': Ddc_refresh.query.filter(Ddc_refresh.id == '2').first().data,

	}
	return render_template('building_11.html', **context)

@app.route('/search/',methods=['GET','POST'])
def search():
	q = request.args.get('q')
	p = request.args.get('p')
	alldata = Ddc_data.query.filter(and_(Ddc_data.DDC_ID==q),Ddc_data.biaohao==p).order_by('-endtime').all()
	context = {
		'alldata': alldata,
		'data_page': (len(Ddc_data.query.order_by('-endtime').all()) / 16) + 1,
		'data_state_1': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[7],
		'data_state_2': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[5],
		'data_state_3': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[6],
		'data_state_4': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[4],
		'data_state_5': Ddc_refresh.query.filter(Ddc_refresh.id == '1').first().data,
		'data_state_6': Ddc_refresh.query.filter(Ddc_refresh.id == '2').first().data,
	}
	return render_template('building_11.html', **context)

@app.route('/jump/',methods=['GET','POST'])
def jump():
	q = request.args.get('q')
	a = int(q)
	alldata = Ddc_data.query.order_by('-endtime').all()[16*(a-1) : 16*a]

	context = {
		'alldata': alldata,
		'data_page': (len(Ddc_data.query.order_by('-endtime').all()) / 16) + 1,
		'data_state_1': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[7],
		'data_state_2': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[5],
		'data_state_3': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[6],
		'data_state_4': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[4],
		'data_state_5': Ddc_refresh.query.filter(Ddc_refresh.id == '1').first().data,
		'data_state_6': Ddc_refresh.query.filter(Ddc_refresh.id == '2').first().data,
	}



	return render_template('building_11.html', **context)

@app.route('/light_switch1/',methods=['POST'])
def light_switch1():
	result = Ddc_state.query.filter(Ddc_state.id == '1').first()
	open_close = result.zhuangtaizi[7]
	if open_close=='1':
		result.mark1='1'
		result.mark2='1'
		result.sign='L10'
		db.session.commit()
	else:
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'L11'
		db.session.commit()
	return redirect(url_for('building_11'))

@app.route('/light_switch2/',methods=['POST'])
def light_switch2():
	result = Ddc_state.query.filter(Ddc_state.id == '1').first()
	open_close = result.zhuangtaizi[5]
	if open_close == '1':
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'L20'
		db.session.commit()
	else:
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'L21'
		db.session.commit()
	return redirect(url_for('building_11'))

@app.route('/fan_switch1/',methods=['POST'])
def fan_switch1():
	result = Ddc_state.query.filter(Ddc_state.id == '1').first()
	open_close = result.zhuangtaizi[6]
	if open_close == '1':
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'F10'
		db.session.commit()
	else:
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'F11'
		db.session.commit()
	return redirect(url_for('building_11'))

@app.route('/fan_switch2/',methods=['POST'])
def fan_switch2():
	result = Ddc_state.query.filter(Ddc_state.id == '1').first()
	open_close = result.zhuangtaizi[4]
	if open_close == '1':
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'F20'
		db.session.commit()
	else:
		result.mark1 = '1'
		result.mark2 = '1'
		result.sign = 'F21'
		db.session.commit()
	return redirect(url_for('building_11'))

@app.route('/building_11_new/')
def building_11_new():
	context = {
		'alldata': Ddc_refresh.query.all(),
		'data_page': (len(Ddc_data.query.order_by('-endtime').all()) / 16) + 1,
		'data_state_1': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[7],
		'data_state_2': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[5],
		'data_state_3': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[6],
		'data_state_4': Ddc_state.query.filter(Ddc_state.id == '1').first().zhuangtaizi[4],
		'data_state_5': Ddc_refresh.query.filter(Ddc_refresh.id == '1').first().data,
		'data_state_6': Ddc_refresh.query.filter(Ddc_refresh.id == '2').first().data,
	}
	return render_template('building_11_new.html', **context)

@app.route('/search_want/',methods=['POST'])
def search_want():
	ddcid = request.form.get('ddcid')
	biaohao = request.form.get('biaohao')
	result = Ddc_data.query.filter(Ddc_data.DDC_ID == ddcid, Ddc_data.biaohao == biaohao).first()
	result.cmd1 = '1'
	result.cmd2 = '1'
	db.session.commit()
	return redirect(url_for('building_11_new'))

@app.route('/search_all/',methods=['POST'])
def search_all():
	result = Ddc_data.query.filter(Ddc_data.id == '1').first()
	result.cmdall1 = '1'
	db.session.commit()
	return redirect(url_for('building_11_new'))

@app.route('/ddc_manage_1/')
@login_required
def ddc_manage_1():
	context1 = {
		'alldata1': Ddc_info.query.all()
	}
	return render_template('ddc_manage_1.html', **context1)

@app.route('/delete/<data_id_1>')
def delete(data_id_1):
	data_id_result = Ddc_info.query.filter(Ddc_info.id == data_id_1).first()
	db.session.delete(data_id_result)
	db.session.commit()
	return redirect(url_for('ddc_manage_1'))

@app.route('/ddc_manage_2/',methods=['GET','POST'])
@login_required
def ddc_manage_2():
	if request.method == 'GET':
		return render_template('ddc_manage_2.html')
	else:
		data1 = request.form.get('data1')
		data2 = request.form.get('data2')
		repeat_confirm1 = Ddc_info.query.filter(Ddc_info.DDC_ID == data1).first()
		if repeat_confirm1:
			return u'该DDC_ID已存在，请重新输入新的DDC_ID！'
		else:
			DDC_info = Ddc_info(DDC_ID=data1,address=data2,biaohao = 'None',number='0',type='None',flag1='1',flag2='1')
			db.session.add(DDC_info)
			db.session.commit()
			return redirect(url_for('ddc_manage_1'))

@app.route('/ddc_manage_3/',methods=['GET','POST'])
@login_required
def ddc_manage_3():
	if request.method == 'GET':
		return render_template('ddc_manage_3.html')
	else:
		data1 = request.form.get('data1')
		data2 = request.form.get('data2')
		data3 = request.form.get('data3')
		repeat_confirm1 = Ddc_info.query.filter(Ddc_info.DDC_ID == data1).first()
		if data1[0] == 'A':
			type_dec = '电表'
		elif data1[0] == 'B':
			type_dec = '水表'
		elif data1[0] == 'C':
			type_dec = '煤气表'
		else:
			type_dec = '其他表具'
		if repeat_confirm1:
			if repeat_confirm1.address == data2:
				if len(data3) == 5:
					if repeat_confirm1.biaohao=='None' and repeat_confirm1.type=='None':
						repeat_confirm1.biaohao = data3
						repeat_confirm1.type = type_dec
						repeat_confirm1.flag1 = '1'
						repeat_confirm1.flag2 = '1'
						db.session.commit()
						return redirect(url_for('ddc_manage_1'))
					else:
						DDC_info = Ddc_info(DDC_ID=data1, address=data2, biaohao=data3, type=type_dec, flag1='1',
						                    flag2='1')
						db.session.add(DDC_info)
						db.session.commit()
						return redirect(url_for('ddc_manage_1'))
				else:
					return u'表号长度与标准不符，请确认后再添加！'
			else:
				return u'该地址与DDC_ID所在的地址不符，请确认后再添加！'
		else:
			return u'该DDC_ID不存在，请添加以后再添加表号！'






@app.route('/regist/',methods=['GET','POST'])
def regist():
	if request.method == 'GET':
		return render_template('regist.html')
	else:
		email = request.form.get('email')
		username = request.form.get('username')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		level = request.form.get('level')
		user = User.query.filter(User.email == email).first()
		if user:
			return u'该邮箱已被注册，请更换邮箱！'
		else:
			if password1 != password2:
				return u'两次密码不相等，请核对后再输入。'
			else:
				user = User(email=email, username=username, password=password1,level=level)
				db.session.add(user)
				db.session.commit()
				return redirect(url_for('over_looking'))

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form.get('username')
		password = request.form.get('password')
		user = User.query.filter(User.username == username, User.password == password).first()
		if user:
			session['user_id'] = user.id
			session.permanent = True
			return redirect(url_for('over_looking'))
		else:
			return u'邮箱或者密码错误，请确认后重新登陆。'

@app.route('/logout/')
def logout():
	session.clear()
	return redirect(url_for('login'))

@app.context_processor
def my_context_processor():
	user_id = session.get('user_id')
	if user_id:
		user = User.query.filter(User.id == user_id).first()
		if user:
			return {'user':user}
	return {}

if __name__ == '__main__':
	app.run()