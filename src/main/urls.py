from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view()),
    path('scored/', views.scored.as_view()),
]