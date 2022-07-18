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
