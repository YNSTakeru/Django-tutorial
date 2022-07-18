# 記事を表示

`mysite/views.py`

```python
from blog.models import Article
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # 全ての記事を取ってくる
    objs = Article.objects.all()
    context = {
        "title": 'Really Site',
        'articles': objs
    }
    return render(request, 'mysite/index.html', context)

```

`templates/mysite/index.html`

```html
<h3 class="pb-4 font-italic border-bottom">Djangoを触ってみた</h3>
{% for obj in articles %}
<div class="blog-post">
    <h2 class="blog-post-title">{{obj.title}}</h2>
    <p class="blog-post-meta">
        {{obj.created_at}} by
        <a href="#">{{obj.author}}</a>
    </p>
    <p>{{obj.text}}</p>
</div>
{% endfor %}
```

`ターミナル`

`templates`フォルダ直下に`blog`フォルダを作成

```bash
mkdir templates/blog
touch templates/blog/article.html
cp templates/mysite/index.html templates/blog/article.html
```

`templates/blog/article.html`

```html
{% extends 'mysite/base.html' %} {% block content %}

<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic border-bottom">Djangoを触ってみた</h3>
            {% for obj in articles %}
            <div class="blog-post">
                <h2 class="blog-post-title">{{obj.title}}</h2>
                <p class="blog-post-meta">
                    {{obj.created_at}} by
                    <a href="#">{{obj.author}}</a>
                </p>
                <p>{{obj.text}}</p>
            </div>
            {% endfor %}
            <nav class="blog-pagination">
                <a class="btn btn-outline-primary" href="#">古い記事</a>
                <a class="btn btn-outline-primary disabled" href="#"
                    >新しい記事</a
                >
            </nav>
        </div>
        <aside class="col-md-4">
            <div class="p-4 mb-3 bg-light rounded">
                <h4 class="font-italic">YNSについて</h4>
                <p class="mb-0">ようこそDjango道場へ！</p>
            </div>
        </aside>
    </div>
</main>

{% endblock %}
```

`blog/views.py`

```python
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def article(request):
    context = {}
    return render(request, 'blog/article.html', context)

```

`blog/urls.py`

```python
from django.urls import include, path

from . import views

urlpatterns = [
    # blog/articleのパスでarticle関数を実行
    path("article/", views.article),
]
```

`blog/urls/py`

```python
from django.urls import include, path

from . import views

urlpatterns = [
    # path("test/", views.test),
    # テーブルのIDを渡す blog直下のパスの値がpkの変数としてarticle関数にわたる
    path('<slug:pk>/', views.article)
]
```

`blog/views.py`

```python
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article


# Create your views here.
def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj
    }
    return render(request, 'blog/article.html', context)

```

`templates/blog/article.html`

```html
{% extends 'mysite/base.html' %} {% block content %}
<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic">{{article.title}}</h3>
            <p class="small text-muted text-right">
                {{article.created_at}} {{article.author}}
            </p>
            <p>{{article.text}}</p>
        </div>
        <aside class="col-md-4">
            <div class="p-4 mb-3 bg-light rounded">
                <h4 class="font-italic">YNSについて</h4>
                <p class="mb-0">ようこそDjango道場へ！</p>
            </div>
        </aside>
    </div>
</main>

{% endblock %}
```

`templates/mysite/index.html`

stretched-link で div で囲ってる範囲すべてを a タグに

```html
{% for obj in articles %}
<div class="blog-post">
    <h2 class="blog-post-title">{{obj.title}}</h2>
    <p class="blog-post-meta">
        {{obj.created_at}} by
        <a href="#">{{obj.author}}</a>
    </p>
    <p>{{obj.text}}</p>
    <a href="/blog/{{obj.id}}" class="stretched-link">続きはこちら</a>
</div>
<hr />
{% endfor %}
```

# 記事一覧ページ作成

`blog/views.py`

```python
def index(request):
    objs = Article.objects.all()
    context = {
        'articles': objs,
    }
    return render(request, 'blog/blogs.html', context)
```

`ターミナル`

```bash
touch templates/blog/blogs.html
```

`templates/blog/blogs.html`

```html
{% extends 'mysite/base.html' %} {% block content %}
<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic">{{article.title}}</h3>
            <p class="small text-muted text-right">
                {{article.created_at}} {{article.author}}
            </p>
            <p>{{article.text}}</p>
        </div>
        <aside class="col-md-4">
            <div class="p-4 mb-3 bg-light rounded">
                <h4 class="font-italic">YNSについて</h4>
                <p class="mb-0">ようこそDjango道場へ！</p>
            </div>
        </aside>
    </div>
</main>

{% endblock %}
```

`blog/urls.py`

```python
urlpatterns = [
    # blogパスにアクセスするとblog/views.pyのindex関数を呼び出す
    path("", views.index),
    path('<slug:pk>/', views.article)
]
```

# ページネーション

`blog/views.py`

```python
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article


def index(request):
    objs = Article.objects.all()
    # 第二引数は1ページに表示する記事の数を表す
    paginator = Paginator(objs, 2)
    # https://example.com/blog/page=1みたいな感じで取得
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)


def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj
    }
    return render(request, 'blog/article.html', context)

```

`templates/blog/blogs.html`

articles を page_obj に

```html
{% for obj in page_obj %}
<div class="blog-post">
    <h2 class="blog-post-title">{{obj.title}}</h2>
    <p class="blog-post-meta">
        {{obj.created_at}} by
        <a href="#">{{obj.author}}</a>
    </p>
    <p>{{obj.text}}</p>
    <a href="/blog/{{obj.id}}" class="stretched-link">続きはこちら</a>
</div>
<hr />

{% endfor %}
```

`templates/blog/blogs.html`

```html
{% extends 'mysite/base.html' %} {% block content %}
<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic border-bottom">Djangoを触ってみた</h3>
            {% for obj in page_obj %}
            <div class="blog-post">
                <h2 class="blog-post-title">{{obj.title}}</h2>
                <p class="blog-post-meta">
                    {{obj.created_at}} by
                    <a href="#">{{obj.author}}</a>
                </p>
                <p>{{obj.text}}</p>
                <a href="/blog/{{obj.id}}" class="">続きはこちら</a>
            </div>
            <hr />

            {% endfor %}
            <nav class="blog-pagination">
                <div class="pagination">
                    <span class="step-links">
                        {% if page_obj.has_previous %}
                        <a class="btn btn-outline-primary" href="?page=1"
                            >&laquo; first</a
                        >
                        <a
                            class="btn btn-outline-primary"
                            href="?page={{ page_obj.previous_page_number }}"
                            >previous</a
                        >
                        {% endif %} {% if page_obj.has_next %}
                        <a
                            class="btn btn-outline-primary"
                            href="?page={{ page_obj.next_page_number }}"
                            >next</a
                        >
                        <a
                            class="btn btn-outline-primary"
                            href="?page={{ page_obj.paginator.num_pages }}"
                            >last &raquo;</a
                        >
                        {% endif %}
                    </span>
                </div>
            </nav>
        </div>
        <aside class="col-md-4">
            <div class="p-4 mb-3 bg-light rounded">
                <h4 class="font-italic">YNSについて</h4>
                <p class="mb-0">ようこそDjango道場へ！</p>
            </div>
        </aside>
    </div>
</main>

{% endblock %}
```

`templates/mysite/snippets/header.html`

```html
<div class="container">
    <header class="py-3">
        <div class="row flex-nowrap justify-content-center align-item-center">
            <div class="col-4 text-center">
                <h1 class="display-4 font-italic">
                    <!-- aタグ化 -->
                    <a href="/" class="text-decoration-none">ReallySite</a>
                </h1>
            </div>
        </div>
    </header>
    <div class="py-1 mb-2">
        <nav class="nav d-flex justify-content-between">
            <!-- hrefに値を追加 -->
            <a class="p-2 link-secondary" href="/blog/">ブログ</a>
            <a class="p-2 link-secondary" href="#">お問い合わせ</a>
            <a class="p-2 link-secondary" href="#">メニュー３</a>
        </nav>
    </div>
</div>
```

`templates/mysite/index.html`

```html
{% for obj in articles %}
<div class="blog-post">
    <h2 class="blog-post-title">{{obj.title}}</h2>
    <p class="blog-post-meta">
        {{obj.created_at}} by
        <a href="#">{{obj.author}}</a>
    </p>
    <p>{{obj.text}}</p>
    <!-- stretched-linkを削除 -->
    <a href="/blog/{{obj.id}}" class="">続きはこちら</a>
</div>
<hr />

{% endfor %}
```

`templates/mysite/index.html`

```html
<nav class="blog-pagination">
    <a class="btn btn-outline-primary" href="/blog/">ブログ一覧はこちら</a>
</nav>
```

`mysite/views.py`

```python
def index(request):
    # 前方3個までを取ってくる
    objs = Article.objects.all()[:3]
    context = {
        "title": 'Really Site',
        'articles': objs
    }
    return render(request, 'mysite/index.html', context)
```

## index.html の aside タグをスニペット化

`ターミナル`

```bash
touch templates/mysite/snippets/sidebar.html
```

`templates/mysite/snippets/sidebar.html`

```html
<aside class="col-md-4">
    <div class="p-4 mb-3 bg-light rounded">
        <h4 class="font-italic">YNSについて</h4>
        <p class="mb-0">ようこそDjango道場へ！</p>
    </div>
</aside>
```

`templates/mysite/index.html`

```html
{% extends 'mysite/base.html' %} {% block content %}

<div class="container">
    <div class="p-4 p-md-5 mb-4 rounded bg-warning">
        <div class="col-md-6 px-0">
            <h1 class="display-4 font-italic">Django道場</h1>
            <p class="lead my-3">文章をかこう</p>
            <p class="lead mb-0">
                <a href="#" class="font-weight-bold">続きを読む</a>
            </p>
        </div>
    </div>
    <div class="row mb-2">
        <div class="col-md-6">
            <div
                class="row g-0 border rounded overflow-hidden flex-md-row
            mb-4 shadow-sm h-md-250 position-relative"
            >
                <div class="col p-4 d-flex flex-column position-static">
                    <strong class="d-inline-block mb-2 text-primary"
                        >Django</strong
                    >
                    <h3 class="mb-0">人気の記事</h3>
                    <div class="mb-1 text-muted">7/17</div>
                    <p class="card-text mb-auto">文章をかこう</p>
                    <a href="#" class="stretched-link">続きを読む</a>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div
                class="row g-0 border rounded overflow-hidden flex-md-row
            mb-4 shadow-sm h-md-250 position-relative"
            >
                <div class="col p-4 d-flex flex-column position-static">
                    <strong class="d-inline-block mb-2 text-primary"
                        >Django</strong
                    >
                    <h3 class="mb-0">人気の記事</h3>
                    <div class="mb-1 text-muted">7/17</div>
                    <p class="card-text mb-auto">文章をかこう</p>
                    <a href="#" class="stretched-link">続きを読む</a>
                </div>
            </div>
        </div>
    </div>
</div>

<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic border-bottom">Djangoを触ってみた</h3>

            {% for obj in articles %}
            <div class="blog-post">
                <h2 class="blog-post-title">{{obj.title}}</h2>
                <p class="blog-post-meta">
                    {{obj.created_at}} by
                    <a href="#">{{obj.author}}</a>
                </p>
                <p>{{obj.text}}</p>
                <a href="/blog/{{obj.id}}" class="">続きはこちら</a>
            </div>
            <hr />

            {% endfor %}

            <nav class="blog-pagination">
                <a class="btn btn-outline-primary" href="/blog/"
                    >ブログ一覧はこちら</a
                >
            </nav>
        </div>
        <!-- この行を追加 -->
        {% include 'mysite/snippets/sidebar.html' %}
    </div>
</main>

{% endblock %}
```

`templates/blog/article.html`

```html
{% extends 'mysite/base.html' %} {% block content %}
<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic">{{article.title}}</h3>
            <p class="small text-muted text-right">
                {{article.created_at}} {{article.author}}
            </p>
            <p>{{article.text}}</p>
        </div>

        <!-- asideタグを変更 -->
        {% include mysite/snippets/sidebar.html' %}
    </div>
</main>

{% endblock %}
```

`ターミナル`

```bash
touch templates/mysite/snippets/pagination.html
```

`templates/mysite/snippets/pagination.html`

```html
<nav class="blog-pagination">
    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
            <a class="btn btn-outline-primary" href="?page=1">&laquo; first</a>
            <a
                class="btn btn-outline-primary"
                href="?page={{ page_obj.previous_page_number }}"
                >previous</a
            >
            {% endif %} {% if page_obj.has_next %}
            <a
                class="btn btn-outline-primary"
                href="?page={{ page_obj.next_page_number }}"
                >next</a
            >
            <a
                class="btn btn-outline-primary"
                href="?page={{ page_obj.paginator.num_pages }}"
                >last &raquo;</a
            >
            {% endif %}
        </span>
    </div>
</nav>
```

`templates/blog/blogs.html`

```html
{% extends 'mysite/base.html' %} {% block content %}
<main class="container">
    <div class="row">
        <div class="col-md-8">
            <h3 class="pb-4 font-italic border-bottom">Djangoを触ってみた</h3>
            {% for obj in page_obj %}
            <div class="blog-post">
                <h2 class="blog-post-title">{{obj.title}}</h2>
                <p class="blog-post-meta">
                    {{obj.created_at}} by
                    <a href="#">{{obj.author}}</a>
                </p>
                <p>{{obj.text}}</p>
                <a href="/blog/{{obj.id}}" class="">続きはこちら</a>
            </div>
            <hr />

            {% endfor %}
            <!-- pagination.htmlに置き換え -->
            {% include 'mysite/snippets/pagination.html' %}
        </div>
        <!-- asideタグをsidebar.htmlに置き換え -->
        {% include 'mysite/snippets/sidebar.html' %}
    </div>
</main>

{% endblock %}
```
