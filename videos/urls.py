from django.conf.urls import url
from .views import list_videos

urlpatterns = [
    url(r'^list$', list_videos, name='list_videos'),
]
