from django.test import TestCase, Client
from django.urls import resolve, reverse
import requests
from appstager.models import Action, Show
from appstager.forms import ActionForm, ShowForm

# create a client
client = Client()

# Test if the views exist and return a 200 status code
class StagerViewTests(TestCase):
	def test_login_view(self):
		response = self.client.get(reverse('appstager:start'))
		self.assertEqual(response.status_code, 200)

	def test_planner_view(self):
		response = self.client.get(reverse('appstager:index'))
		self.assertEqual(response.status_code, 200)

	def test_shows_view(self):
		response = self.client.get(reverse('appstager:index'))
		self.assertEqual(response.status_code, 200)

# Test AJAX views
class StagerAjaxTests(TestCase):
	# ensure the returned action form populates with correct argument
	def test_create_action(self):
		url = reverse('appstager:createAction', args=('Vibrate',))
		response = self.client.get(url)
		self.assertContains(response, 'Vibrate')

	# test an invalid ActionForm submission
	# show is not a string
	def test_action_form_invalid(self):
		form = ActionForm( {
			'show': "Show1",
			'action_type': "Image",
			'name': "rab",
			'description': "This is an image",
			'order': 1,
			'duration': 0,
		})
		self.assertFalse(form.is_valid())

	# test a valid ShowForm submission
	def test_show_form_valid(self):
		form = ShowForm( {
			'name': "Phantom of the Opera",
			'director': "Andrew Lloyd Webber",
		})
		self.assertTrue(form.is_valid())

	# test an invalid ShowForm submission
	# show names must be unique
	def test_show_form_invalid(self):
		show = Show.objects.create(name = 'Phantom of the Opera', director = 'rab')

		form = ShowForm( {
			'name': "Phantom of the Opera",
			'director': "Andrew Lloyd Webber",
		})
		self.assertFalse(form.is_valid())


class StagerAPITests(TestCase):
	def test_api_running(self):
		try:
			res=requests.post('http://localhost:4000/shows?name=kalo&director=kale1')
		except requests.exceptions.RequestException:
			self.fail("API Not running")
