from django.test import TestCase
from .models import Image,Category,Location


class ImageTestClass(TestCase):
  def setup(self):
    self.new_image = Image(title = 'jandta',
     description = "sparta ",
    location=self.new_location,
    category=self.new_category,
    image='image.jpeg')

  def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

  def test_instance_(self):
   self.assertTrue(isinstance(self.new_image, Image))

  def test_save_image(self):
    self.new_image.save_image()

  def test_delete_image(self):
    self.new_image.save_image()
    self.new_image.delete_image()

  def test_search_image(self,category):
      self.new_image.save_image()
      image =  Category.objects.filter(category=category)
      self.assertTrue(image)

  
class CategoryTestClass(TestCase):
    def setUp(self):
        self.Sky = Category(title = 'sky')
        self.sky.save_title()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Sky, Category))

    def test_save_category(self):
        self.test_category = Category(title= 'Travel')
        self.test_category.save_title()
        self.test_category.delete_title()

class LocationTestClass(TestCase):
    def setUp(self):
        self.singapore = Location(title='Miami')
        self.singapore.save_title()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.singapore,Location))

    def test_save_location(self):
        self.singapore.save_title()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_delete_method(self):
        self.singapore.delete_title()
        Station = Location.objects.all()
        print(Station)
        self.assertTrue(len(Station)==0)
