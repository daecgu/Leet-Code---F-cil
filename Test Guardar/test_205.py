from .solution import Solution
# from .solution import *


class Test205:

    def test_same_len(self):
        sol = Solution()
        assert sol.same_len("s", "t") == True
        assert sol.same_len("so", "t") == False
        assert sol.same_len("s", "to") == False

    def test_same_ammount_different_characters(self):
        sol = Solution()
        assert sol.same_ammount_different_characters("a","b") == True
        assert sol.same_ammount_different_characters("ab","bb") == False

    def test_len_key_map_s_to_t_eq(self):
        sol = Solution()
        assert sol.mapeo("sos", "tto") == False
        assert sol.mapeo("paper", "title") == True


    def test_is_isomorphic(self):
        sol = Solution()
        assert sol.isIsomorphic("ab", "ccc") == False
        assert sol.isIsomorphic("ab", "cc") == False
        assert sol.isIsomorphic("s", "t") == True
        assert sol.isIsomorphic("s", "t") == True
        assert sol.isIsomorphic("sos", "tto") == False




