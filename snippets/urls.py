from django.conf.urls import url
from .views import play_snippets

urlpatterns = [
    url(r'^snippets/(/d+)$', play_snippets, name='play_snippets'),
]
