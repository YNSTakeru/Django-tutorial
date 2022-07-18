# Bootstrap5 の設定

`templates/mysite/base.html`

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
        {% block content %}{% endblock %}
        <script
            src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
            integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
            crossorigin="anonymous"
        ></script>
        <script
            src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js"
            integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/"
            crossorigin="anonymous"
        ></script>
    </body>
</html>
```

`templates/mysite/index.html`

```html
{% extends 'mysite/base.html' %} {% block content %}

<div class="container">
    <header class="py-3">
        <div class="row flex-nowrap justify-content-center align-item-center">
            <div class="col-4 text-center">
                <h1 class="display-4 font-italic">ReallySite</h1>
            </div>
        </div>
    </header>
    <div class="py-1 mb-2">
        <nav class="nav d-flex justify-content-between">
            <a class="p-2 link-secondary" href="#">ブログ</a>
            <a class="p-2 link-secondary" href="#">お問い合わせ</a>
            <a class="p-2 link-secondary" href="#">メニュー３</a>
        </nav>
    </div>
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
            <div class="blog-post">
                <h2 class="blog-post-title">サンプル</h2>
                <p class="blog-post-meta">
                    2022/7/17 by
                    <a href="#">YNS</a>
                </p>
            </div>
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

<footer class="border-top py-5 text-center bg-light mt-4">
    <p>
        <a href="/">トップに戻る</a>
    </p>
</footer>

{% endblock %}
```

# index.html をきれいにわける

`templates/mysite/base.html`

index.html の header と footer を base.html に移植

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
        <div class="container">
            <header class="py-3">
                <div
                    class="row flex-nowrap justify-content-center align-item-center"
                >
                    <div class="col-4 text-center">
                        <h1 class="display-4 font-italic">ReallySite</h1>
                    </div>
                </div>
            </header>
            <div class="py-1 mb-2">
                <nav class="nav d-flex justify-content-between">
                    <a class="p-2 link-secondary" href="#">ブログ</a>
                    <a class="p-2 link-secondary" href="#">お問い合わせ</a>
                    <a class="p-2 link-secondary" href="#">メニュー３</a>
                </nav>
            </div>
        </div>

        {% block content %}{% endblock %}

        <footer class="border-top py-5 text-center bg-light mt-4">
            <p>
                <a href="/">トップに戻る</a>
            </p>
        </footer>
        <script
            src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
            integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
            crossorigin="anonymous"
        ></script>
        <script
            src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js"
            integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/"
            crossorigin="anonymous"
        ></script>
    </body>
</html>
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
            <div class="blog-post">
                <h2 class="blog-post-title">サンプル</h2>
                <p class="blog-post-meta">
                    2022/7/17 by
                    <a href="#">YNS</a>
                </p>
            </div>
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

## snippets フォルダを作成

base.html の header と footer を snippets フォルダに移植

`ターミナル`

```bash
mkdir templates/mysite/snippets
touch templates/mysite/snippets/header.html
touch templates/mysite/snippets/footer.html
```

`templates/mysite/snippets/header.html`

```html
<div class="container">
    <header class="py-3">
        <div class="row flex-nowrap justify-content-center align-item-center">
            <div class="col-4 text-center">
                <h1 class="display-4 font-italic">ReallySite</h1>
            </div>
        </div>
    </header>
    <div class="py-1 mb-2">
        <nav class="nav d-flex justify-content-between">
            <a class="p-2 link-secondary" href="#">ブログ</a>
            <a class="p-2 link-secondary" href="#">お問い合わせ</a>
            <a class="p-2 link-secondary" href="#">メニュー３</a>
        </nav>
    </div>
</div>
```

`templates/mysite/snippets/footer.html`

```html
<footer class="border-top py-5 text-center bg-light mt-4">
    <p>
        <a href="/">トップに戻る</a>
    </p>
</footer>

<script
    src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
    crossorigin="anonymous"
></script>
<script
    src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js"
    integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/"
    crossorigin="anonymous"
></script>
```

`templates/mysite/snippets/base.html`

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
