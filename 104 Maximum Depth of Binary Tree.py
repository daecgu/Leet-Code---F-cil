# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def busqueda_profundidad(unNodo, profundidad=0):
            if not unNodo:
                return profundidad

            Max_profundidad = profundidad
            profundidad += 1

            return max(busqueda_profundidad(unNodo.left, profundidad), busqueda_profundidad(unNodo.right, profundidad))

        return busqueda_profundidad(root, 0)