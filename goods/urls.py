#coding=utf-8
from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^$', views.ShowIndex.as_view()),
    url(r'^category/(\d+)$', views.ShowIndex.as_view()),
    url(r'^category/(\d+)/page/(\d+)$', views.ShowIndex.as_view()),
    url(r'^goodsdetails/(\d+)$', views.DetailView.as_view())
]