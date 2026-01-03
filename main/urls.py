from django.urls import path
from . import views

urlpatterns = [
    path('api/packages/', views.package_list_create),
    path('api/packages/<int:pk>/ready/', views.set_package_ready),
]