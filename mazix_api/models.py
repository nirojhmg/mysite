from django.db import models
class Category(models.Model):
  name = models.CharField(max_length=30)
  file = models.FileField(blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Wallpaper(models.Model):
  name = models.CharField(max_length=30)
  category = models.ForeignKey(to=Category,on_delete=models.CASCADE, related_name="category", null=True, blank=True)
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  downloads= models.IntegerField(default=0)
  def __str__(self):
    return self.name