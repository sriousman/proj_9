import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Menu, Item, Ingredient

# Model Tests

def create_ingredient():
    return


def create_item():
    return


def create_menu():
    return


class IngredientModelTests(TestCase):
    def setUp(self):
        pass

    def test_ingredient_string(self):
        pass


class ItemModelTests(TestCase):
    def setUp(self):
        pass

    def test_item_string(self):
        pass

    def test_item_creation_date(self):
        pass

    def test_related_items_by_chef(self):
        pass


class MenuModelTests(TestCase):
    def setUp(self):
        pass

    def test_menu_string(self):
        pass

    def test_menu_created_date(self):
        pass

    def test_menu_expiration_date(self):
        pass


# View Tests

class MenuViewTests(TestCase):
    def setUp(self):
        pass

    def test_menu_list_view(self):
        pass

    def test_menu_detail_view(self):
        pass

    def test_menu_creation_alerts(self):
        pass

    def test_menu_deletion_alerts(self):
        pass


class ItemViewTests(TestCase):
    def setUp(self):
        pass

    def test_item_list_view(self):
        pass

    def test_item_detail_view(self):
        pass

    def test_item_creation_alerts(self):
        pass

    def test_item_deletion_alerts(self):
        pass


class IngredientViewTests(TestCase):
    def setUp(self):
        pass

    def test_ingredient_list_view(self):
        pass

    def test_ingredient_detail_view(self):
        pass

