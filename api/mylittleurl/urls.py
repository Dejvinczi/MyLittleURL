from django.urls import path

from .views import LittleURLListCreateAPIView, LittleURLRetrieveDestroyAPIView

urlpatterns = [
    path('', LittleURLListCreateAPIView.as_view()),
    path('<str:little_url>', LittleURLRetrieveDestroyAPIView.as_view()),
]
