from .solution import Solution
import pytest
# from .solution import *


class Test661:
    def test_avg(self):
        img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
        solucion = Solution()
        assert solucion.avg_filtro(img, 0, 0) == 137

    def test_solucion(self):
        img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
        solucion = Solution()
        assert solucion.imageSmoother(img) == [[137,141,137],[141,138,141],[137,141,137]]
