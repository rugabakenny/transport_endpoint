from django.urls import path
from views import *
from .import views
urlspatterns=[
    path('', views.welcome, name =''),
    path('post-data/',views.posts,name='posts')
]
