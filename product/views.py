from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import Brand, Category, Product, ProductLine

# Create your views here.


class CatagoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Category
    """

    queryset = Category.objects.all().order_by("-id")

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        quaryset = self.queryset
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Brand
    """

    queryset = Brand.objects.all().order_by("-id")

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        quaryset = self.queryset
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Brand
    """

    queryset = Product.objects.all().order_by("-id")

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        quaryset = self.queryset
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductLineViewSet(viewsets.ViewSet):
    
    
    queryset = ProductLine.objects.all().order_by("-id")

    @extend_schema(responses=ProductLineSerializer)
    def list(self, request):
        quaryset = self.queryset
        serializer = ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)
