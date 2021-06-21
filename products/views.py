from django.shortcuts import render
from rest_framework import viewsets, response, status
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products =  Products.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def retreive(self, request, id=None):
        pass
    def update(self, request, id=None):
        pass
    def delete(self, request, id=None):
        pass
