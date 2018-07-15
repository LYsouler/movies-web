# coding:utf8
from . import home
from flask import render_template, redirect, url_for

'''
@home.route("/")
def index():
    return render_template("home/index.html")
'''


@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))


@home.route("/regist/")
def regist():
    return render_template("home/regist.html")


# 会员中心
@home.route("/user/")
def user():
    return render_template("home/user.html")


# 修改密码
@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")


# 评论记录
@home.route("/comments/")
def comments():
    return render_template("home/comments.html")


# 登录日志
@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")


# 收藏电影
@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")


# 电影
@home.route("/")
def index():
    return render_template("home/index.html")


# 动画
@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


# 搜索
@home.route("/search/")
def search():
    return render_template("/home/search.html")


# 详情
@home.route("/play/")
def play():
    return render_template("home/play.html")
