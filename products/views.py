from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish
from .serializers import ProductSerializers
from .models import Products, User
import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products =  Products.objects.all()
        serializer = ProductSerializers(products, many=True)
        publish()
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
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
        publish('product_updated', pk)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response("product deleted", status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
