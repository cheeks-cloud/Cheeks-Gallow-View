from django.db import models
from django.shortcuts import get_object_or_404

class Location(models.Model):
    name = models.CharField( max_length=30,null=False, blank=False)

    def __str__(self):
      return self.name

class Category(models.Model):
    CHOICES = [
        ('Nature', 'Nature'),
        ('Sky', 'Sky'),
        ('Animals', 'Animals'),
        ('People', 'People'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Vehicles', 'Vehicles'),
        ('People', 'People'),
        
    ]

    category = models.CharField( choices=CHOICES, max_length=30,null=False, blank=False)

    def __str__(self):
      return self.category

class Image(models.Model):
  image = models.ImageField(null=False, blank=False, upload_to='images/')
  image_name = models.CharField(max_length=40,null=False, blank=False)
  image_description = models.TextField(null=False, blank=False)
  location = models.ForeignKey(Location, on_delete = models.CASCADE)
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
 
  # class Meta:
  #   ordering = ['image_location']
  def save_image(self):
    self.save()

  def delete_image(self):
     Image.objects.get(id = self.id).delete()

  def update_image(self,val):
      Image.objects.filter(id = self.id).update(image=val)

  @classmethod
  def get_image_by_id(cls, image_id):
    return cls.objects.filter(cls,id=image_id)

  @classmethod
  def search_image(cls, category):
    try:
      image_to_find = Category.objects.filter(category=category)
      return cls.objects.filter(category_id = image_to_find.id)
    except Exception:
      return 'image not found'

  @classmethod
  def filter_by_location(cls,location):
    image_by_location = Location.objects.get(location = location)
    return cls.objects.filter(location_id = image_by_location.id) 

  def __str__(self):
      return self.image_name

