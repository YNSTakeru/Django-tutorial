# Python 環境構築

-   Python Version
    -   3.9.7

`ターミナル`

```bash
mkdir newFolder
cd new Folder
python -m venv venv
source venv/bin/activate
pip install django
```

もし以下の画像の WARNING が表示されたら

![pipのupgrade画像](images/1.png)

以下のコマンドを実行

`ターミナル`

```bash
pip install --upgrade pip
```

# プロジェクト作成

ディレクトリ直下に config プロジェクトを作成

```
django-admin startproject config .
```
