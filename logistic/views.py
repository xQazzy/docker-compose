from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = CustomPageNumberPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [filters.SearchFilter]
    search_fields = ['address', 'products__title', 'products__description']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Stock.objects.all()
        product_id = self.request.query_params.get('products')
        if product_id:
            queryset = queryset.filter(products__id=product_id)
        return queryset
