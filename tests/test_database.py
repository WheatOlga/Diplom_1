
import pytest
from unittest.mock import patch
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    
    def test_database_initialization(self, mock_bun_class, mock_ingredient_class):
       
        database = Database()

        assert mock_bun_class.call_count == 3
        
        mock_bun_class.assert_any_call("black bun", 100)
        mock_bun_class.assert_any_call("white bun", 200)
        mock_bun_class.assert_any_call("red bun", 300)

        assert mock_ingredient_class.call_count == 6
        
        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_FILLING, "dinosaur", 200)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_buns_returns_list(self, mock_bun_class, mock_ingredient_class):

        database = Database()
        buns = database.available_buns()
        
        assert isinstance(buns, list)
        assert len(buns) == 3

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_ingredients_returns_list(self, mock_bun_class, mock_ingredient_class):

        database = Database()
        ingredients = database.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        