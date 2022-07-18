# Blog アプリケーション作成

`ターミナル`

```bash
# startappする際は一度ローカルサーバーを落とす
python manage.py startapp blog
```

`config/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "livereload",
    'django.contrib.staticfiles',
    'mysite',
    'blog'
]

```

`config/urls.py`

```python
urlpatterns = [
    path("", views.index),
    # blogのパスにアクセスしたらblog/urls.pyが読み込まれる
    path("blog/", include("blog.urls"))
]
```

`ターミナル`

```bash
touch blog/urls.py
```

`blog/urls.py`

```python
from django.urls import include, path

from . import views

urlpatterns = [
    # blogの中のviews.pyのtest関数
    path("test/", views.test),
]
```

`blog/views.py`

```python
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):
    return HttpResponse("test page")

```

`ターミナル`

```bash
# blog/testパスにアクセス
python manage.py runserver
```

## アクセス順序

-   config/urls.py
-   blog/urls.py
-   blog/views.py
