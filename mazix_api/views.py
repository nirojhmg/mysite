from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import (Category,Wallpaper)
from .serializers import (CategorySerializer,WallpaperSerializer)

class CategoryView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)



class WallpaperView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        wallpeper_serializer = WallpaperSerializer(data=request.data)
        if wallpeper_serializer.is_valid():
            wallpeper_serializer.save()
            return Response(wallpeper_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(wallpeper_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
            wallpapers = Wallpaper.objects.all()
            serializer = WallpaperSerializer(wallpapers, many=True)
            return Response(serializer.data)


