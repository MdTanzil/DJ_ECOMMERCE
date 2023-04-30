from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import Brand, Category, Product, ProductLine
from rest_framework.decorators import action

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

    @action(
        methods=["get"],
        detail=False,
        url_path="category/(?P<category>\w+)/all",
        url_name="all",
    )
    def list_product_by_catagory(self, request, category=None):
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )
        return Response(serializer.data)


class ProductLineViewSet(viewsets.ViewSet):
    queryset = ProductLine.objects.all().order_by("-id")

    @extend_schema(responses=ProductLineSerializer)
    def list(self, request):
        quaryset = self.queryset
        serializer = ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)
