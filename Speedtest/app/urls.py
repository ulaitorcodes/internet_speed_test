from django.urls import path

from .views import post_collection

urlpatterns = [
    path('', post_collection, name="speed"),
]
