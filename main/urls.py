from django.urls import path
from . import views

urlpatterns = [
    path('api/packages/', views.package_list_create, name='package-list-create'),
    path('api/packages/<int:pk>/', views.package_detail, name='package-detail'),
]