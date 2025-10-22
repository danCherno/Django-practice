from django.urls import path, include
from practiceApi import views

from rest_framework.routers import DefaultRouter

from practiceApi import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
