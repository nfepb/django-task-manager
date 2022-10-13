from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):

    # Self refers to TestDjango because it inherits TestCase class
    def test_this_thing_works(self):
        self.assertEqual(1, 1)
