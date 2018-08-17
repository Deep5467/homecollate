from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.post_new, name='post_new'),
    url(r'^pg/', views.new_pg, name='new_pg')
]