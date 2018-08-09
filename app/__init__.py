# coding:utf-8
from flask import Flask

from app.models.base import db
from flask_login import LoginManager

# 登录管理器
login_manager = LoginManager()

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

#创建一个应用服务
def create_app():
    app = Flask(__name__, static_url_path='/static')
    # print(__name__)    应用的根路径：app, 静态文件路径从此开始
    # 导入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 给app 注册蓝图
    register_blueprint(app)


    # 注册登录管理器
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录'

    # Models
    db.init_app(app)
    # 使current_app生效：将应用上下文入栈
    with app.app_context():
        # db.drop_all()
        db.create_all()
    return app