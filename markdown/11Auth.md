# 認証機能の実装

`config/urls.py`

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    # ログインパスを追加
    path("login/", views.login),
    path("blog/", include("blog.urls"))
]

```

`mysite/views.py`

```python
def login(request):
    context = {}
    return render(request, "mysite/login.html", context)
```

`ターミナル`

```bash
touch templates/mysite/login.html
# 認証のテンプレートを別途作る
touch templates/mysite/base_auth.html
```

`templates/mysite/base_auth.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link
            rel="stylesheet"
            href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css"
            integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I"
            crossorigin="anonymous"
        />
        <title>ReallySite</title>
    </head>

    <body>
        {% include 'mysite/snippets/header.html' %} {% block content %}{%
        endblock %} {% include 'mysite/snippets/footer.html' %}
    </body>
</html>
```

## head タグの中身をスニペット化

`ターミナル`

```bash
touch templates/mysite/snippets/head.html
```

`templates/mysite/snippets/head.html`

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css"
    integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I"
    crossorigin="anonymous"
/>
<title>ReallySite</title>
```

`templates/mysite/base_auth.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        {% include 'mysite/snippets/head.html' %}
    </head>

    <body
        class="vh-100 d-flex align-items-center justify-content-center bg-light"
    >
        {% block content %}{% endblock %}
    </body>
</html>
```

`templates/mysite/base.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        {% include 'mysite/snippets/head.html' %}
    </head>

    <body>
        {% include 'mysite/snippets/header.html' %} {% block content %}{%
        endblock %} {% include 'mysite/snippets/footer.html' %}
    </body>
</html>
```

`templates/mysite/login.html`

```html
{% extends 'mysite/base_auth.html' %} {% block content %}
<div class="container ">
    <div class="row">
        <div class="col-lg-3 m-auto ">
            <h1 class="display-4 font-italic text-center ">
                <a href="/" class="text-decoration-none">ReallySite</a>
            </h1>
        </div>
        <div class="col-lg-3 m-auto ">
            <form class="form-signin mx-4">
                <div class="text-center">
                    <h1 class="h5 my-4 ">ログイン</h1>
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="email"
                        id="id_email"
                        class="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                    />
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="password"
                        id="id_password"
                        class="form-control"
                        placeholder="Password"
                        required="required"
                    />
                </div>

                <button class="btn btn-primary btn-block my-3" type="submit">
                    サインイン
                </button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
```

# POST 送信

`templates/mysite/login.html`

```html
<!-- method属性を追加 -->
<form class="form-signin mx-4" method="POST">
    <div class="text-center">
        <h1 class="h5 my-4 ">ログイン</h1>
    </div>

    <div class="form-label-group my-3">
        <input
            type="email"
            id="id_email"
            class="form-control"
            placeholder="Email address"
            required="required"
            autofocus="autofocus"
        />
    </div>

    <div class="form-label-group my-3">
        <input
            type="password"
            id="id_password"
            class="form-control"
            placeholder="Password"
            required="required"
        />
    </div>

    <button class="btn btn-primary btn-block my-3" type="submit">
        サインイン
    </button>
</form>
```

## POST の値を確認

`mysite/views.py`

```python
def login(request):
    context = {}
    if request.method == 'POST':
        context['req'] = request.POST
    return render(request, "mysite/login.html", context)
```

`templates/mysite/login.html`

```html
{% extends 'mysite/base_auth.html' %} {% block content %}
<div class="container ">
    <div class="row">
        <div class="col-lg-3 m-auto ">
            <h1 class="display-4 font-italic text-center ">
                <a href="/" class="text-decoration-none">ReallySite</a>
            </h1>
        </div>
        <div class="col-lg-3 m-auto ">
            <!-- POSTされたかのテスト -->
            {{ req }}

            <form class="form-signin mx-4" method="POST">
                <!-- CSRF対策 -->
                {% csrf_token %}
                <div class="text-center">
                    <h1 class="h5 my-4 ">ログイン</h1>
                </div>

                <div class="form-label-group my-3">
                    <!-- name属性を追加してPOSTに流す -->
                    <input
                        type="email"
                        id="id_email"
                        name="email"
                        class="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                    />
                </div>

                <div class="form-label-group my-3">
                    <!-- name属性を追加してPOSTに流す -->
                    <input
                        type="password"
                        id="id_password"
                        name="password"
                        class="form-control"
                        placeholder="Password"
                        required="required"
                    />
                </div>

                <button class="btn btn-primary btn-block my-3" type="submit">
                    サインイン
                </button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
```

`/login/`パスでアクセス

# LoginView

`mysite/views.py`

```python
from blog.models import Article
# LoginViewで簡単にログインの機能を実装
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    objs = Article.objects.all()[:3]
    context = {
        "title": 'Really Site',
        'articles': objs
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/login.html'

```

`mysite/urls.py`

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    # ログインパスを書き換え
    path("login/", views.Login.as_view()),
    path("blog/", include("blog.urls"))
]
```

# ログインしたかどうかを判断する

`templates/mysite/login.html`

```html
{% extends 'mysite/base_auth.html' %} {% block content %}
<div class="container ">
    <div class="row">
        <div class="col-lg-3 m-auto ">
            <h1 class="display-4 font-italic text-center ">
                <a href="/" class="text-decoration-none">ReallySite</a>
            </h1>
        </div>
        <div class="col-lg-3 m-auto ">
            <!-- userのデフォルトはanonymous -->
            {% if user.is_authenticated %} ログイン中です {% else %}
            ログインしていません {% endif %}

            <form class="form-signin mx-4" method="POST">
                {% csrf_token %}
                <div class="text-center">
                    <h1 class="h5 my-4 ">ログイン</h1>
                </div>
                <!-- name属性のemailをusernameに変更する。djangoでユーザー認証する際はusernameだから -->
                <div class="form-label-group my-3">
                    <input
                        type="email"
                        id="id_email"
                        name="username"
                        class="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                    />
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="password"
                        id="id_password"
                        name="password"
                        class="form-control"
                        placeholder="Password"
                        required="required"
                    />
                </div>

                <button class="btn btn-primary btn-block my-3" type="submit">
                    サインイン
                </button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
```

ログインするとエラーが発生するのでログインのパスとリダイレクトの設定を追加

`config/settings.py`

```python

# 追加
LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/logout/'

LOGOUT_REDIRECT_URL = '/login/'
```

# ログアウトの追加

`config/urls.py`

```python
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
# from django.urls import path
from django.urls import include, path
from mysite import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("login/", views.Login.as_view()),
    # ログアウトパスの追加
    path("logout/", LogoutView.as_view()),
    path("blog/", include("blog.urls"))
]

```

login.html の検証用の if 文を削除

templates/mysite/login.html

```html
{% extends 'mysite/base_auth.html' %} {% block content %}
<div class="container ">
    <div class="row">
        <div class="col-lg-3 m-auto ">
            <h1 class="display-4 font-italic text-center ">
                <a href="/" class="text-decoration-none">ReallySite</a>
            </h1>
        </div>
        <div class="col-lg-3 m-auto ">
            <form class="form-signin mx-4" method="POST">
                {% csrf_token %}
                <div class="text-center">
                    <h1 class="h5 my-4 ">ログイン</h1>
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="email"
                        id="id_email"
                        name="username"
                        class="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                    />
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="password"
                        id="id_password"
                        name="password"
                        class="form-control"
                        placeholder="Password"
                        required="required"
                    />
                </div>

                <button class="btn btn-primary btn-block my-3" type="submit">
                    サインイン
                </button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
```

# 新規登録機能の追加

`config/urls.py`

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("login/", views.Login.as_view()),
    path("logout/", LogoutView.as_view()),
    path("blog/", include("blog.urls")),
    # サインアップパスの追加
    path('signup/', views.signup)
]

```

`ターミナル`

```bash
touch mysite/forms.py
```

`mysite/forms.py`

```python
from django import forms
from django.contrib.auth import get_user_model


# バリデーションのために追加
class UserCreationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        # ハッシュ化
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

```

## ログインと登録がほとんど一緒なので login.html を使い回す

`mysite/views.py`

```python
from blog.models import Article
# LoginViewで簡単にログインの機能を実装
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render

from mysite.forms import UserCreationForm


def index(request):
    objs = Article.objects.all()[:3]
    context = {
        "title": 'Really Site',
        'articles': objs
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    # login.htmlもauthに変更
    template_name = 'mysite/auth.html'


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # commit=FalseでDBにはまだ登録しない
            user = form.save(commit=False)
            # DBに登録
            user.save()
    return render(request, 'mysite/auth.html', context)

```

`ターミナル`

```bash
mv templates/mysite/login.html templates/mysite/auth.html
```

`templates/mysite/auth.html`

```html
{% extends 'mysite/base_auth.html' %} {% block content %}
<div class="container ">
    <div class="row">
        <div class="col-lg-3 m-auto ">
            <h1 class="display-4 font-italic text-center ">
                <a href="/" class="text-decoration-none">ReallySite</a>
            </h1>
        </div>
        <div class="col-lg-3 m-auto ">
            <form class="form-signin mx-4" method="POST">
                {% csrf_token %}
                <div class="text-center">
                    <h1 class="h5 my-4 ">
                        {% if 'login' in request.path %} ログイン {% elif
                        'signup' in request.path %} 新規登録 {% endif %}
                    </h1>
                </div>

                <div class="form-label-group my-3">
                    <!-- usernameやemailの間に空白を含めない -->
                    <input
                        type="email"
                        id="id_email"
                        name="{% if 'login' in request.path %}username {% elif 'signup' in request.path %}email{% endif %}"
                        class="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                    />
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="password"
                        id="id_password"
                        name="password"
                        class="form-control"
                        placeholder="Password"
                        required="required"
                    />
                </div>

                <button class="btn btn-primary btn-block my-3" type="submit">
                    サインイン
                </button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
```

-   email
    -   test2@gmail.com
-   Password
    -   yalaYa34567oiafjeaio

## 管理画面でも User を新規作成できるように編集 mysite/admin.py の中の 2 ヶ所へ追加

`mysite/admin.py`

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models import User

from mysite.forms import UserCreationForm  # adminでuser作成用に追加

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )
    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )

    add_form = UserCreationForm  # adminでuser作成用に追加


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
```

# 新規登録のリダイレクト

`mysite/views.py`

```python
from blog.models import Article
# この行を追加
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
# この行を変更
from django.shortcuts import redirect, render
from mysite.forms import UserCreationForm


def index(request):
    objs = Article.objects.all()[:3]
    context = {
        "title": 'Really Site',
        'articles': objs
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/auth.html'


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # 登録成功メッセージ
            messages.success(request, "登録完了!!!!")
            # リダイレクト
            return redirect("/")
    return render(request, 'mysite/auth.html', context)


```

`config/settings.py`

```python
AUTH_USER_MODEL = 'mysite.User'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/logout/'

LOGOUT_REDIRECT_URL = '/login/'

# --------- massage tab with bootstrap alert class ---------------------

MESSAGE_TAGS = {
    messages.ERROR: 'rounded-0 alert alert-danger',
    messages.WARNING: 'rounded-0 alert alert-warning',
    messages.SUCCESS: 'rounded-0 alert alert-success',
    messages.INFO: 'rounded-0 alert alert-info',
    messages.DEBUG: 'rounded-0 alert alert-secondary',
}
# --------- massage tab with bootstrap alert class ---------------------
```

`ターミナル`

```bash
touch templates/mysite/snippets/messages.html
```

```html
{% for msg in messages %}
<nav class="py-2 {{ msg.tags }}">
    <div class="container">{{ msg }}</div>
</nav>
{% endfor %}
```

`templates/mysite/base.html`

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        {% include 'mysite/snippets/head.html' %}
    </head>

    <body>
        {% include 'mysite/snippets/header.html' %}
        <!-- この行を追加 -->
        {% include 'mysite/snippets/messages.html' %} {% block content %}{%
        endblock %} {% include 'mysite/snippets/footer.html' %}
    </body>
</html>
```

# Login した時にもメッセージを表示

`mysite/views.py`

```python
from blog.models import Article
from django.contrib import messages
# LoginViewで簡単にログインの機能を実装
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render

from mysite.forms import UserCreationForm


def index(request):
    objs = Article.objects.all()[:3]
    context = {
        "title": 'Really Site',
        'articles': objs
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/auth.html'

    # 以下の行を追加
    def form_valid(self, form):
        messages.success(self.request, "ログイン完了!!!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "エラーあり!!!!")
        return super().form_invalid(form)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "登録完了!!!!")
            return redirect("/")
    return render(request, 'mysite/auth.html', context)

```

# メニューの作成

`templates/mysite/auth.html`

```html
{% extends 'mysite/base_auth.html' %} {% block content %}
<div class="container ">
    <div class="row">
        <div class="col-lg-3 m-auto ">
            <h1 class="display-4 font-italic text-center ">
                <a href="/" class="text-decoration-none">ReallySite</a>
            </h1>
        </div>
        <div class="col-lg-3 m-auto ">
            <form class="form-signin mx-4" method="POST">
                {% csrf_token %}
                <div class="text-center">
                    <h1 class="h5 my-4 ">
                        {% if 'login' in request.path %} ログイン {% elif
                        'signup' in request.path %} 新規登録 {% endif %}
                    </h1>
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="email"
                        id="id_email"
                        name="{% if 'login' in request.path %}username{% elif 'signup' in request.path %}email{% endif %}"
                        class="form-control"
                        placeholder="Email address"
                        required="required"
                        autofocus="autofocus"
                    />
                </div>

                <div class="form-label-group my-3">
                    <input
                        type="password"
                        id="id_password"
                        name="password"
                        class="form-control"
                        placeholder="Password"
                        required="required"
                    />
                </div>

                <button class="btn btn-primary btn-block my-3" type="submit">
                    サインイン
                </button>
            </form>

            <!-- 以下の行を追加 -->
            {% if 'login' in request.path %}
            <div class="text-center">
                <a href="/signup/" class="link-secondary">新規登録はこちら</a>
            </div>
            {% elif 'signup' in request.path %}
            <div class="text-center">
                <a href="/login/" class="link-secondary">ログインはこちら</a>
            </div>
            {% endif %}
        </div>
    </div>
</div>

{% endblock %}
```

## ヘッダーのメニュー 3 を編集

`templates/mysite/snippets/header.html`

```html
<div class="container">
    <header class="py-3">
        <div class="row flex-nowrap justify-content-center align-item-center">
            <div class="col-4 text-center">
                <h1 class="display-4 font-italic">
                    <a href="/" class="text-decoration-none">ReallySite</a>
                </h1>
            </div>
        </div>
    </header>
    <div class="py-1 mb-2">
        <nav class="nav d-flex justify-content-between">
            <a class="p-2 link-secondary" href="/blog/">ブログ</a>
            <a class="p-2 link-secondary" href="#">お問い合わせ</a>

            {% if user.is_authenticated %}
            <a href="/logout/" class="p-2 link-secondary">ログアウト</a>
            {% else %}
            <div>
                <a href="/login/" class="p-2 link-secondary">ログイン</a>
                <a href="/signup/" class="btn btn-outline-info">新規登録</a>
            </div>
            {% endif %}
        </nav>
    </div>
</div>
```
