from django.shortcuts import redirect, render

from oatk_website import models


def index(request):
    template = "pages/index.html"
    context = {}
    return render(request, template, context)


def news(request, page=None):
    starting_index = 0
    if page:
        starting_index = page * 8
    articles = models.News.objects.all().order_by("-publish_date")[starting_index:starting_index+8]
    total_pages = (len(articles) // 8) + 1

    template = "pages/news.html"
    context = {
        "news": articles,
        "current_page": page if page else 1,
        "total_pages": range(1, total_pages + 1),
    }
    return render(request, template, context)
