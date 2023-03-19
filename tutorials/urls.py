# from django.conf.urls import re_path   # url is deprecated & chg to re_path
from django.urls import re_path
from tutorials import views

urlpatterns = [
    re_path(r'^api/tutorials$', views.tutorial_list),
    re_path(r'^api/tutorials/(?P<pk>)[0-9+]$', views.tutorial_detail),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published)
]
