from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Products

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products =  Products.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def retreive(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)    
        
    def update(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializers(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        return Response("product deleted", status=status.HTTP_204_NO_CONTENT)
