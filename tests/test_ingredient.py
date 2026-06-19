import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import data

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)

    def test_ingredient_return_correct_values(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type,name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price