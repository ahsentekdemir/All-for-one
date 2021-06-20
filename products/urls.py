from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('product', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
                
    })),
    path('product/<string:pk>', ProductViewSet.as_view({
        'get': 'retreive',
        'put': 'update',
        'delete': 'delete'
    }))
]
