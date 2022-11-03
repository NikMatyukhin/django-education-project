from django.urls import path

from .views import WorkViewset

urlpatterns = [
    path('works/', WorkViewset.as_view({'get': 'list', 'post': 'create'}), name='works-list'),
    path('works/<int:pk>', WorkViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='works-detail'),
]