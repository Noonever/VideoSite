from django.urls import path
from .views import start_page_view, video_view

urlpatterns = [
    path('', start_page_view, name='start_page'),
    path('<str:code>/', video_view, name='video')
]
