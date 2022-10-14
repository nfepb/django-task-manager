from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):
    item = Item.objects.create(name='Test todo item')
    self.assertFalse(item.done)