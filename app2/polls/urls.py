from django.conf.urls import url
from . import views
from .views import (
    IndexView,
    DetailView,
    ResultView
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name= 'index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name= 'detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', ResultView.as_view(), name= 'results'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name= 'vote'),
]
