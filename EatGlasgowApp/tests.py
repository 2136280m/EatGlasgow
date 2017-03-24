from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

class GeneralTests(TestCase):
    def test_serving_static_review_images(self):
        result = finders.find('images/review_images/defRev.jpg')
        self.assertIsNotNone(result)
    def test_serving_static_restaurant_images(self):
        result = finders.find('images/restaurant_images/defRes.jpg')        self.assertIsNotNone(result)
    def test_serving_static_review_images(self):
        result = finders.find('images/review_images/defUser.jpg')
        self.assertIsNotNone(result)

		
class HomePageTests(TestCase):
    def test_index_contains__AppName(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'EatGlasgow', response.content)
         
    def test_home_using_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'about/')
		
		
class ModelTests(TestCase):
	def setUp(self):
		try:
			from EatGlasgow.models import *
		except ImportError:
			print('The module populate_unibook does not exist')
		except:
			print('Something went wrong in the populate() function :-(')
			
	def get_restaurant(self, resID-ID):
		from EatGlasgow.models import Restaurant
		try:                  
			R = Restaurant.objects.get(resID=resID-ID)
		except Restaurant.DoesNotExist:    
			R = None
		return R
	
		
class ViewTests(TestCase):

	def setUp(self):
		try:
			from forms import UserForm
		
		except ImportError:
			print('The module forms does not exist')
		except NameError:
			print('The class CourseForm does not exist or is not correct')
		except:
			print('Something else went wrong :-(')
	pass