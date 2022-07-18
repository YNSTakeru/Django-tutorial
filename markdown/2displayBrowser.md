# アプリケーションを作成してブラウザに表示する

## アプリケーションの作成

```bash
python manage.py startapp mysite
```

## 各種ファイルについて

-   `admin.py`

    -   管理画面の設定

-   `models.py`

    -   データベースの定義

-   `tests.py`

    -   テストに使用

-   `views.py`
    -   ブラウザで表示される見た目

# `mysite`の `views.py` を表示させる設定をこれから記述していく

`config/urls.py`

## 最初に読み込まれるファイル

```python
from django.contrib import admin
# from django.urls import path
from django.urls import include, path
# mysiteのviewsディレクトリを使う
from mysite import views

# topページのurlをviews.indexで表示する
urlpatterns = [
    path("",views.index),
]
```

`config/settings.py`

`os`ライブラリがインポートされていなければ

```python
import os
```

`mysite` を追加する

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',
]
```

ホストのアクセス設定

```python
# 本番環境では独自のドメインを指定
ALLOWED_HOSTS = ['*']
```

`mysite/views.py`

```python
from django.http import HttpResponse
from django.shortcuts import render

'''
config/urls.pyで設定した
    path("", views.index),
はこのindex関数
'''


def index(request):
    return HttpResponse("hello Really Site")

```

`ターミナル`

```bash
python manage.py runserver
# ctr + C で停止
```

# templates フォルダの作成

```bash
mkdir templates
mkdir templates/mysite
touch templates/mysite/index.html
```

`config/settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # プロジェクト直下のtemplatesフォルダを使えるように
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

`templates/mysite/index.html`

```html
<h1>indexファイルですよ</h1>
```

`mysite/views.py`

```python
from django.shortcuts import render

def index(request):
    '''
    config/settings.jsonで記述した
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
    より相対パスはtemplates/から始まるので
    第二引数はmysite/index.html
    '''
    return render(request, 'mysite/index.html', {})

```

`ターミナル`

```bash
python manage.py runserver
```

# Python から HTML に変数を渡す

`mysite/views.py`

```python
from django.shortcuts import render

def index(request):
    # 辞書型で渡す
    context = {
        "title": 'Really Site'
    }
    return render(request, 'mysite/index.html', context)
```

`templates/mysite/index.html`

```html
<h1>{{ title }}</h1>
```

# 共通部分は base.html などにして使いまわせるようにする

```bash
touch templates/mysite/base.html
```

`base.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <h1>Base.htmlです</h1>
    </body>
</html>
```

`templates/mysite/index.html`

base.html を index.html 内で読み込む

```html
{% extends "mysite/base.html" %}
<h1>extends以下はブラウザに反映されない</h1>
```

`ターミナル`

```bash
python manage.py runserver
```

## `templates/mysite/index.html`の中身を記述する方法

`templates/mysite/base.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <h1>Base.htmlです</h1>
        {% block content %}{% endblock %}
    </body>
</html>
```

`templates/mysite/index.html`

```html
{% extends "mysite/base.html" %} {% block content %}
<h1>index.ファイルですよ</h1>
{% endblock %}
```

`templates/mysite/base.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <div>メニュー</div>
        {% block content %}
        <h1>contentが呼び出されなければこのタグが表示される</h1>
        {% endblock %}
    </body>
</html>
```
