from django.urls import path
from .views import ProductViewSets

urlpatterns = [
    path('products', ProductViewSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSets.as_view({
        'get': 'retrive',
        'put': 'update',
        'delete': 'destroy'
    })),
]