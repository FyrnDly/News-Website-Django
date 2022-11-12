from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:category>', views.category),
    path('<slug:category>/<slug:slugContent>', views.post),
]