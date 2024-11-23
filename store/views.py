from rest_framework import viewsets
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['product_name']
    ordering_fields = ['product_name', 'price', 'created_date']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # Модель Category вместо Product
    serializer_class = CategorySerializer
