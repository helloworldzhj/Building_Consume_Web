#-*-coding:utf-8-*-

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zhuhuajian10_15 import app
from exts import db
from models import User, Ddc_data, Ddc_info, Ddc_state, Ddc_refresh
#只有导入了，它才会把user这个模型导入到数据库中

manager = Manager(app)

migrate = Migrate(app,db)
#使用migrate绑定app和db

manager.add_command('db',MigrateCommand)
#添加迁移脚本的命令到manager中

if __name__ == "__main__":
	manager.run()
































