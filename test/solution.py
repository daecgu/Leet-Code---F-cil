from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        repetidos = []
        for each in nums:
            if each in repetidos:
                return True
            if len(repetidos) == k:
                repetidos.pop(0)
            repetidos.append(each)
        return False

"""
1 2 3 1 2 3
0 1 2 3 4 5
  1 2 3 4 5
    1 2 3 4
      1 2 3
        1 2
          1
"""
stack =[]
new = stack.pop()