from django.db import models

# Create your models here.
class Image(models.Model):
  image = models.ImageField(null=False, blank=False, upload_to='images/')
  image_name = models.CharField(max_length=40,null=False, blank=False)
  image_description = models.TextField(null=False, blank=False)
  image_location = models.ForeignKey('Location', on_delete = models.CASCADE)
  image_ category = models.ForeignKey('Category', on_delete = models.CASCADE)

  def __str__(self):
      return self.image
 
  def save_image(self):
    self.save()

  @classmethod
  def delete_image(self):
    pass

  def update_image(self, new_name, new_description, new_image, new_category, new_location):
      self.image = new_image
      self.image_name = new_name
      self.image_location = new_location
      self.image_description = new_description
      self.image_category = new_category
  def get_image_by_id(self, id):
    pass

  @classmethod
  def search_image(cls, category):
    image_to_find = Image.objects.filter(category=category)
    return image_to_find

  @classmethod
  def filter_by_location(cls,location):
    image_by_location = Image.objects.filter(location=location)
    return image_by_location


class Location(models.Model):
  name = models.ManyToManyField(Image)

  def __str__(self):
      return self.location

class Category(models.Model):
  category = models.CharField(max_length=40)

  def __str__(self):
      return self.category
