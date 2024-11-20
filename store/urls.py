from .views import ProductViewSet, CategoryViewSet
from django.urls import path


urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name='product_list')
]