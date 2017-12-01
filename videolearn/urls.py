"""snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from accounts.views import home_page
from accounts import urls as accounts_urls
from videos import urls as videos_urls
from snippets import urls as snippets_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", home_page, name="home"),
    url(r"^accounts/", include(accounts_urls)),
    url(r"^videos/", include(videos_urls)),
    url(r"^snippets/", include(snippets_urls)),
]
