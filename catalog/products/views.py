from itertools import product
from rest_framework import viewsets, response
from .models import Product
from .serializers import ProductSerializers

class ProductViewSets(viewsets.ViewSet):
    
    def list(self, request): # /api/products
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return response.Response(serializer.data)

    def create(self, request): # /api/products
        pass

    def retrieve(self, pk=None): # /api/products/<str:id>
        pass

    def update(self, pk=None): # /api/products/<str:id>
        pass

    def destroy(self, pk=None): # /api/products/<str:id>
        pass

