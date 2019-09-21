import unittest
import requests
import requests_cache
import json
from functions import *
from secrets import *
from eat_healthy import *


class InstanceTests(unittest.TestCase):
    def test_restaurant_constructor_noattributes(self):
        with self.assertRaises(TypeError):
            testRestaurant=Restaurant()

    def test_restaurant_constructor_noaddress(self):
        with self.assertRaises(TypeError):
            testRestaurant=Restaurant("McDonald's")

    def test_restaurant_constructor_allattributes(self):
        testRestaurant=Restaurant("McDonald's", "123 Main St")
        self.assertIsInstance(testRestaurant, Restaurant)

    def test_menu_item_constructor_noattributes(self):
        with self.assertRaises(TypeError):
            testItem=MenuItem()

    def test_menuitem_constructor_nourl(self):
        testItem=MenuItem("Big Mac")
        self.assertIsInstance(testItem, MenuItem)

    def test_menuitem_constructor_allattributes(self):
        testItem=MenuItem("Big Mac", "test.html")
        self.assertIsInstance(testItem, MenuItem)


class CoordinatesTests(unittest.TestCase):
    def test_getCoordinates_realzip(self):
        testgoodresults=getCoordinates(48313)
        self.assertIs(type(testgoodresults), tuple)

    def test_getCoordinates_fakezip(self):
        testbadresults=getCoordinates(00000)
        self.assertIsNot(type(testbadresults), tuple)

    def test_getCoordinates_string(self):
        testbadresults=getCoordinates("zipcode")
        self.assertIsNot(type(testbadresults), tuple)


class GetChainsTests(unittest.TestCase):
    def test_getchains_goodresults(self):
        test48313=getChains(48313)
        test48313names=[]
        for chain in test48313:
            test48313names.append(chain.name)
        self.assertIn("McDonald's", test48313names)

    def test_getchains_badresults(self):
        with self.assertRaises(TypeError):
            test00000=getChains(00000)


class getMenuItemsTests(unittest.TestCase):
    def setUp(self):
        self.mcdonalds=Restaurant("McDonald's", "123 Main Street")
        self.fakechain=Restaurant("fjdalkwueuruubuszzz", "123 Main Street")

    def test_getmenuitems_goodresults(self):
        test_mcdonalds_menu=getMenuItems(self.mcdonalds)
        test_menu=[]
        for food in test_mcdonalds_menu:
            test_menu.append(food.title)
        self.assertIn("Big Mac", test_menu)
        self.assertIn("Sausage Biscuit", test_menu)

    def test_getmenutems_badresults(self):
        test_bad_call=getMenuItems(self.fakechain)
        self.assertEqual(len(test_bad_call),0)

    def tearDown(self):
        del self.mcdonalds
        del self.fakechain


if __name__ == '__main__':
    unittest.main(verbosity=2)
