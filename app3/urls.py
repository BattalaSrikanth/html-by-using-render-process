from django.urls import path
from app3.views import *
app_name='srikanth'
urlpatterns=[
    path('srikanth/',srikanth,name='srikanth'),
]