# helloworld 20160724
# coding=utf-8
from flask_script import Manager
from flask import Flask
app = Flask(__name__)
manager=Manager(app)

# url 路由与方法
@app.route('/')
def index():
	return '<h1>Hello World!</h1>'
	
# 新增方法Get方式传值
# 尖括号中的值就是Get的变量值
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello,%s!</h1>' % name

# 启动服务器
if __name__ =='__main__':
	manager.run()