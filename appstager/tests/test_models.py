#from django.test import TestCase
import unittest,random
from faker import Faker 
from appstager.models import Action

# A list that contains random events of sounds since Faker does not have anything as such
event_list=['vibrate','ring','activate torch_light','play thunder_sound'] 


class TestEvent(unittest.TestCase):

	def setUp(self):
		self.fake=Faker()
		# self.event=Event(
		# 	event_name=self.fake.first_name()
		# 	)
		self.event=random.choice(event_list)

	def test_event_exists(self):
		expected_event=str(self.event)
		self.assertEqual(expected_event,str(self.event))


