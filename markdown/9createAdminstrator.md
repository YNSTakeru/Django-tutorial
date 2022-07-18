# 管理画面の確認

`ターミナル`

```bash
python manage.py runserver
```

## 管理画面の URL を設定

`config/urls.py`

```python
urlpatterns = [
    # adminへのパスを追加
    path("admin/", admin.site.urls),
    path("", views.index),
    path("blog/", include("blog.urls"))
]
```

## 管理者の作成

`ターミナル`

```python
python manage.py createsuperuser
```

-   email
    -   test@gmail.com
-   password
    -   2022717uwoO0o

`blog/admin.py`

管理者画面に Blog/Articles が追加される

```python
from django.contrib import admin

from blog.models import Article

admin.site.register(Article)
```

<h2 style="color:yellow">管理画面で適当に記事を 2 個作成しておく<span style="color:red">!</span>
</h2>
