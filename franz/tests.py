from django.test import TestCase
from .models import FurnitureType, Furniture, FurnitureDetails
from django.contrib.auth.models import User
from franz.forms import FurnitureForm

# Create your tests here.
class FurnTypeTest(TestCase):
    def setUp(self):
        self.type=FurnitureType(typeName='Couch', typeDescription='Test Value')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Couch')

    def test_tablename(self):
        self.assertEqual(str(FurnitureType._meta.db_table), 'furnituretype')

class FurnitureTest(TestCase):
    def setUp(self):
        self.type = FurnitureType(typeName='Chair')
        self.user = User(username='user1')
        self.furn = Furniture(furnitureName='TestBrand', furnitureType=self.type, user=self.user, dateEntered='2021-06-25 15:31', furniturePrice='299.99')
        
    def test_string(self):
        self.assertEqual(str(self.furn), 'TestBrand')

class NewFurnitureForm(TestCase):
    def setUp(self):
        self.user = User(username='user1')
        self.type = FurnitureType(typeName='Table')
        self.mruser = self.user
        #Failing
    def test_furnitureform(self):
        form=FurnitureForm(data={'furnitureName':'TestTable', 'furnitureType':self.type, 'user':self.mruser, 'dateEntered':'2021-06-28 12:30', 'furniturePrice':'359.99', 'furnitureDescription':'TESTTESTTESTTESTdescription'})
        self.assertTrue(form.is_valid())
        #Failing
    def test_min_furnitureform(self):
        form=FurnitureForm(data={'furnitureName':'Test Table', 'typeName':'Table', 'user':'JohnM', 'dateEntered':'2021-06-28 12:30'})
        self.assertTrue(form.is_valid())

    def test_empty_furnitureform(self):
        form=FurnitureForm(data={'furnitureName': ''})
        self.assertFalse(form.is_valid())
