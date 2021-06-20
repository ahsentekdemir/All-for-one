from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products =  Products.objects.all()
        serializers = ProductSerializers
    def create(self, request):
        pass
    def retreive(self, request, id=None):
        pass
    def update(self, request, id=None):
        pass
    def delete(self, request, id=None):
        pass
