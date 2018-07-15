# coding:utf8
'''
注册蓝图
'''
from flask import Flask,render_template

app = Flask(__name__)
app.debug = True
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
'''
后面的
  url_prefix前缀是访问是的链接
'''
app.register_blueprint(admin_blueprint, url_prefix="/admin")


# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
