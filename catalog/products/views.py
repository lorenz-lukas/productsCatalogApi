from .models import Product
from .serializers import ProductSerializers
from rest_framework import response, status, viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ProductViewSets(viewsets.ViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.
    
    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    serializer_class = ProductSerializers

    def list(self, request): # /api/products
        products = Product.objects.all()
        # self.__logger.info("Products: {}".format(products))
        serializer = ProductSerializers(products, many=True)
        return response.Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT, 
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                'image': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            }
        )
    )
    def create(self, request): # /api/products
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, pk=None): # /api/products/<str:id>
        pass

    def update(self, pk=None): # /api/products/<str:id>
        pass

    def destroy(self, pk=None): # /api/products/<str:id>
        pass

