from django.test import TestCase

from .models import *
# Create your tests here.

class ImageTest(TestCase):

    # # def class instance setup for the project
    # def setUp(self):
    #     self.nairobi = Location(name='nairobi')
    #     self.nairobi.save()
    #
    #     self.nature = Category(name='nature')
    #     self.nature.save()
    #
    #     self.new_image = Image(name="New Image",description="An Image",location=self.nairobi,category=self.nature)
    #     self.new_image.save()
    #
    # # def a testcase for instance of the drinks class
    def test_instance(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))
#
#     def test_delete_image(self):
#         self.drinks.save()
#         self.drinks.delete()
#         self.assertTrue(len(Image.objects.all()) == 0)
#
#     def test_update(self):
#         self.drinks.save()
#         self.drinks.name = 'MoreDrinks'
#         self.assertTrue(self.drinks.name == 'MoreDrinks')
#
#     def test_all_images(self):
#         self.drinks.save()
#         images = Image.all_images()
#         self.assertTrue(len(images) > 0)
#
#     def test_search_by_category(self):
#         self.drinks.save()
#         images = Image.search_by_category('fun')
#         self.assertTrue(len(images) > 0)
#
#     def test_view_location(self):
#         self.drinks.save()
#         location = Image.view_location(self.nairobi)
#         self.assertTrue(len(location) > 0)
#
#     def test_view_category(self):
#         self.drinks.save()
#         categories = Image.view_category(self.music)
#         self.assertTrue(len(categories) > 0)

class CategoriesTest(TestCase):
    def setUp(self):
        self.nature = Category(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))

    def test_save(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

class LocationTest(TestCase):
    def setUp(self):
        self.nairobi = Location(name='nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)
