from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('leave_review', views.leave_review, name='leave_review'),
]