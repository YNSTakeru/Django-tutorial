# ホットライブラリでブラウザをリロードせずに反映させよう

`ターミナル`

```bash
pip install django-livereload-server
```

`config/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload', # staticfilesの前に挿入
    'django.contrib.staticfiles',
    'mysite',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "livereload.middleware.LiveReloadScript",  # livereload
]

```

`ターミナル`を 2 個起動する

`ターミナル 1`

```bash
python manage.py runserver
```

`ターミナル 2`

```bash
python manage.py livereload
```

## エラーが出たら

OSError: [Errorno 48] Address already in use

```python
LIVERELOAD_PORT = "8080"
```
