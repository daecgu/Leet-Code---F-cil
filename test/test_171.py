from .solution import Solution


class Test171:
    def test_check_letter(self):
        sol = Solution()
        assert sol.titleToNumber('A') == 1
        assert sol.titleToNumber('B') == 2
        assert sol.titleToNumber('Z') == 26

    def test_two_letters(self):
        sol = Solution()
        assert sol.titleToNumber('AA') == 27
        assert sol.titleToNumber('AB') == 28
        assert sol.titleToNumber('ZY') == 701

    def test_three_leters(self):
        sol = Solution()
        assert sol.titleToNumber('AAA') == 703
        assert sol.titleToNumber('AAB') == 704