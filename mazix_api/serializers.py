from rest_framework import serializers
from .models import (Category,Wallpaper)
class CategorySerializer(serializers.ModelSerializer):
  class Meta():
    model = Category
    fields = ('id', 'name','file', 'timestamp')

class WallpaperSerializer(serializers.ModelSerializer):
  class Meta():
    model = Wallpaper
    fields = ('id', 'name','category','file', 'timestamp','downloads')