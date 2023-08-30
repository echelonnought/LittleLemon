from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Eru", price=555, inventory=100)
        self.assertEqual(str(item), "Eru : 555 : 100")