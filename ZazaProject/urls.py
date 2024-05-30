from django.urls import path

from ZazaProject.views import index

urlpatterns = [
    path('', index),
]