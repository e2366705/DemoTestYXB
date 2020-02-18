

'''



YXB


第一步: 安装
打开 Windows 的cmd , 输入指令:
pip install Django==3.0.3 -i https://pypi.tuna.tsinghua.edu.cn/simple

还可以从Github进行源码安装, 这里不再赘述, 网上有教程

查看 Django 是否安装成功?
cmd输入:
python -m django --version


创建一个项目 (DemoTestYXB 为创建的项目名称):
django-admin startproject DemoTestYXB



创建一个应用 (vvv1 为应用的名称):
python manage.py startapp vvv1

在 settings.py 里面注册你新建的应用

在应用 vvv1 下面, 新建一个 Templates 文件夹(注意, 必须是这个名称, 是固定写法),
然后新建一个html文档 , index.html



启动 Django 里面内置的服务器:
python manage.py runserver localhost:8866







'''