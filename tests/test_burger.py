
import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import data

class TestBurger:

    def test_set_buns(self):

        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):

        burger = Burger()
        ingredient = Ingredient("FILLING", "Meat", 800)
        
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):

        burger = Burger()
        ingredient_1 = Ingredient("FILLING", "Meat", 100.0)
        ingredient_2 = Ingredient("SAUCE", "Ketchup", 50.0)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        
        burger.remove_ingredient(0)

        assert ingredient_1 not in burger.ingredients
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_2

    def test_move_ingredient_with_mock(self):

        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        
        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_3
        assert burger.ingredients[2] == mock_ingredient_1

    def test_get_price(self):

        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient_1 = Ingredient("FILLING", "Meat", 50)
        ingredient_2 = Ingredient("SAUCE", "Ketchup", 30)
        
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        
        assert burger.get_price() == 280

    def test_get_receipt(self):

        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient_1 = Ingredient("SAUCE", "Hot Sauce", 50)
        ingredient_2 = Ingredient("FILLING", "Cutlet", 100)
        
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        
        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce Hot Sauce =\n"
            "= filling Cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 350"
        )
        assert receipt == expected_receipt
