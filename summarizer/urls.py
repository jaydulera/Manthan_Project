from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='summarizer-home'),
    path('about/',views.about, name='summarizer-about'),
]