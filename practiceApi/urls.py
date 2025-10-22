from django.urls import path
from practiceApi import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
