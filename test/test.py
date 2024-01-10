from .solution import Solution
import pytest
# from .solution import *


class Test219:
    def test_repetidos(self):
        solucion = Solution()
        assert solucion.containsNearbyDuplicate([1,2,3,1,2,3], 3) == True
        assert solucion.containsNearbyDuplicate([1,2,3,1,4,5], 3) == False
        assert solucion.containsNearbyDuplicate([1,2,3], 2) == False
