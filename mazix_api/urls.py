from django.conf.urls import url
from .views import (CategoryView,WallpaperView)
urlpatterns = [
  url(r'^category/$', CategoryView.as_view(), name='mazix'),
  url(r'^wallpaper/$', WallpaperView.as_view(), name='mazix'),

]