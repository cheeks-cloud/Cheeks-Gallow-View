from django.db import models

# Create your models here.
class Image(models.Model):
  image = models.ImageField()
  image_name = models.CharField(max_length=40)
  image_description = models.TextField()
  image_location = models.ForeignKey('Location', on_delete = models.CASCADE)
  category = models.ForeignKey('Category', on_delete = models.CASCADE)

  def __str__(self):
      return self.image
 
  def save_image(self):
    pass

  def delete_image(self):
    pass

  def update_image(self, image):
    pass

  def get_image_by_id(self, id):
    pass

  @classmethod
  def search_image(category):
    pass

  @classmethod
  def filter_by_location(location):
    pass


class Location(models.Model):
  location = models.ManyToManyField(Image)
  def __str__(self):
      return self.location

class Category(models.Model):
  category = models.CharField(max_length=40)

  def __str__(self):
      return self.category
