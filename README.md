# stu

学生成绩管理系统



系统部署说明



学号              姓名

\[233401010226]        \[李厚绍]

\[233401010124]        \[吴海明]



项目地址: https://github.com/xiaowu59/stu





技术栈声明



后端: Python 3.x + Flask

前端: HTML + CSS + JavaScript

数据库: MySQL





本地部署步骤



1\. 数据库初始化



CREATE DATABASE stu;

USE stu;



2\. 后端启动



cd stu

pip install flask flask-sqlalchemy pymysql

python app.py



3\. 前端启动



cd frontend

npm install

npm run dev



前端访问地址: http://localhost:5173



4\. 测试账号



管理员: admin / 123456

普通学生: stu001 / 123456





功能模块



用户注册与登录

成绩 CRUD 操作

课程管理

