"""games URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from games.settings import BASE_DIR, MEDIA_ROOT
from mytest.views import index, contact, game_review, post, single_game_review, single_post
from loginapp.views import login, logout, register
import os


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index, name='index'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url(r'^user/', include('loginapp.urls')),
    url(r'^login$', login, name='login'),
    url(r'^register$', register, name='register'),
    url(r'^logout$', logout, name='logout'),
    url(r'^contact/', contact, name='contact'),
    url(r'^game_review/', game_review, name='game_review'),
    url(r'^post/', post, name='post'),
    url(r'^single_game_review/', single_game_review, name='single_game_review'),
    url(r'^single_post/', single_post, name='single_post'),
    url(r'^captcha', include('captcha.urls')),
]
