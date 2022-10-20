from django.urls import path

from .views import rendering, index, jsonify


urlpatterns = [
    path('hello/', index),
    path('jsonify/', jsonify),
    path('rendering/', rendering),
]
