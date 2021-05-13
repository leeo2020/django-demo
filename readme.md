Django基本命令：

安装Django： pip install django  指定版本 pip3 install django==2.0

新建项目： django-admin.py startproject mysite

新建APP : python manage.py startapp blog

启动：python manage.py runserver 8080

同步或者更改生成 数据库：

python manage.py makemigrations

python manage.py migrate

清空数据库： python manage.py flush

创建管理员： python manage.py createsuperuser

修改用户密码： python manage.py changepassword username

Django项目环境终端： python manage.py shell

这个命令和 直接运行 python 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据的测试非常方便。