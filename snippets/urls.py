from django.conf.urls import url
from .views import list_snippets

urlpatterns = [
    url(r'^snippets', list_snippets, name='list_snippets'),
]
