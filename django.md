# Django

要使用Django，首先需要建立一个虚拟工作环境。虚拟环境是系统的一个位置，你可以在其中安装包，并将其与其他Python包隔离。

## 1. 虚拟环境

### 2.1 创建虚拟环境

新建一个目录，并在目录新建虚拟环境，执行：

```py
python3 -m venv ll_env
```

上面的代码运行了模块venv，并使用它来创建一个名为ll_env的虚拟环境。
（老的版本需要安装virtualenv环境，这里是python3，可以直接使用venv）

### 2.2 激活/关闭 虚拟环境

建立虚拟环境后，需要使用下面的命令激活它：

```py
source ll_env/bin/activate
```

执行成功，命令行即进入 `(ll_env)locallibrary mac$` 的环境中。在这种情况下，你可以在环境中安装包，并使用已安装的包。你在ll_env中安装的包仅在该环境处于活动状态时才可用。

如要停止虚拟环境，则可以执行：

```py
deactivate
```

即可退出虚拟环境的激活状态。

<br />

## 2. 安装 Django

在激活的虚拟环境下，安装 Django ：

```cmd
pip install Django
```

接下来等待 Django 安装，安装成功后，就可以使用 Django 来创建项目了。Django 使用 `django-admin startproject` 来创建项目：

```cmd
django-admin startproject locallibrary .
```

> 注意，需要在项目的后面加入句号 `.` ，否则部署应用程序时将遭遇一些配置问题。如果忘记了这个句点，就将创建的文件和文件夹删除（ll_env除外），再重新运行这个命令。

创建成功后，就可以看到 `locallirary` 目录以及里面的文件.它还创建了一个名为 `manage.py` 的文件，这是一个简单的程序，它接受命令并将其交给Django的相关部分去运行.

> 目录 locallirary包含4个文件，其中最重要的是settings.py、urls.py和wsgi.py。文件settings.py指定Django如何与你的系统交互以及如何管理项目。在开发项目的过程中，我们将修改其中一些设置，并添加一些设置。文件urls.py告诉Django应创建哪些网页来响应浏览器请求。文件wsgi.py帮助Django提供它创建的文件，这个文件名是web server gateway interface（Web服务器网关接口）的首字母缩写。

<br />

安装成功后，就可以使用下面的命令来试试是否安装成功：

```cmd
python3 manage.py runserver
```

如果顺利的话，访问 127.0.0.1 即可看到项目。
<br />

## 3. 安装 SQLite 数据库

> SQLite是一种使用单个文件的数据库，是编写简单应用程序的理想选择，因为它让你不用太关注数据库管理的问题。

在项目中创建 SQLite 数据库，需要运行：

```cmd
python3 manage.py migrate
```

执行后，将会在目录中生成一个 db.sqlite3 文件，并与该项目匹配。




