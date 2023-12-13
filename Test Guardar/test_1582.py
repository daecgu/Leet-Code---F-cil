from .solution import Solution
import pytest
# from .solution import *


class Test1582:
    def test_contar_especiales(self):
        solucion = Solution()
        mat = [[1, 0], [0, 1]]
        mat1 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]

        assert solucion.numSpecial(mat) == 2
        assert solucion.numSpecial(mat1) == 1

    def test_unos_en_fila(self):
        solucion = Solution()
        mat = [[1, 1], [0, 1]]
        mat1 = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]

        assert solucion.unos_en_fila(0, mat) == 2
        assert solucion.unos_en_fila(0, mat1) == 2

    def test_unos_en_columna(self):
        solucion = Solution()
        mat = [[1, 1], [0, 1]]
        mat1 = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]

        assert solucion.unos_en_columna(0, mat) == 1
        assert solucion.unos_en_columna(0, mat1) == 2

    def test_solo_en_fila(self):
        solucion = Solution()
        mat = [[1, 0], [0, 1]]
        mat1 = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]

        assert solucion.solo_en_fila(0,0, mat) == True
        assert solucion.solo_en_fila(0,0, mat1) == False

    def test_solo_en_columna(self):
        solucion = Solution()
        mat = [[1, 0], [0, 1]]
        mat1 = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]

        assert solucion.solo_en_columna(0,0, mat) == True
        assert solucion.solo_en_columna(0,0, mat1) == False