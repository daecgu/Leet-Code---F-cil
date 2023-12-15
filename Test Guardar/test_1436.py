from .solution import Solution
import pytest
# from .solution import *


class Test1436:
    def test_convertir_a_diccionario(self):
        solucion = Solution()
        paths = [["London", "New York"],["New York", "Lima"],["Lima", "Sao Paulo"]]

        diccionario = solucion.convertir_a_diccionario(paths)

        assert type(diccionario) == dict
        assert diccionario["London"] == "New York"
        assert "Sao Paulo" in diccionario.values()

    def test_not_in_key(self):
        paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        assert "Sao Paulo" not in paths

