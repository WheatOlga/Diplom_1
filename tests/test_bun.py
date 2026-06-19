import pytest
from praktikum.bun import Bun
import data

class TestBun:

    @pytest.mark.parametrize("name, price", data.BUNS)

    def test_bun_return_correct_values(self, name, price):
        bun = Bun(name, price)
        
        assert bun.get_name() == name
        assert bun.get_price() == price

