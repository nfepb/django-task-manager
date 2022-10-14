from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    # Self refers to TestItemForm because it inherits TestCase class
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.error.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
