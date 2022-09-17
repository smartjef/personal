from . import views
from django.urls import path
app_name='portfolio'
urlpatterns=[
    path('',views.portfolio, name='portfolio')
]