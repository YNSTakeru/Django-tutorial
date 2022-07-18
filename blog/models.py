from django.db import models

# Create your models here.

'''
Article -> テーブル名
title -> 列名
'''


class Article(models.Model):
    # nullを入れないためにdefaultを渡す
    title = models.CharField(
        default="",
        max_length=30)

    text = models.TextField(default="",)

    author = models.CharField(default="", max_length=30)

    # 自動で追加される
    created_at = models.DateField(auto_now_add=True)

    updated_at = models.DateField(auto_now=True)
