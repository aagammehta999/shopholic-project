from .models import Category
from django.http import request

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)
