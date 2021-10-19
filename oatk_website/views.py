from django.shortcuts import redirect, render

from oatk_website import models


def index(request):
    return render(request, "pages/index.html", {})
