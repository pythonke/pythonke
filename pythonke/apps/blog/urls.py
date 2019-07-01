from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name="list"),
    path('create', views.post_create),
    re_path(r'^(?P<pk>\d+)/$', views.post_detail, name="detail"),
    re_path(r'^(?P<pk>\d+)/edit/$', views.post_update, name="update"),
    re_path(r'^(?P<pk>\d+)/delete/$', views.post_delete, name="delete"),
]
