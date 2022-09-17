from . import views
from django.urls import path

app_name='resume'
urlpatterns=[
    path('',views.resume, name='resume'),
]