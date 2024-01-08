# Recursividad
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(ramaA, ramaB):
            if not ramaA and not ramaB:
                return True
            if not ramaA or not ramaB:
                return False
            if ramaA.val == ramaB.val:
                return symmetric(ramaA.left, ramaB.right) and symmetric(ramaA.right,ramaB.left)
            else:
                return False

        return symmetric(root.left, root.right)

# Iteratividad
from collections import deque


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # creamos una cola a la que le añadimos la raíz dos veces
        queue = deque([root, root])

        while queue:
            # quitamos dos valores de la cola y los guardamos en variables, son los nodos que visitaremos
            nodo1 = queue.popleft()
            nodo2 = queue.popleft()

            # si los Nodos son None, volvemos al principio del bucle while
            if not nodo1 and not nodo2:
                continue
            # si uno de los nodos es None y el otro no se devuelve falso ya que no son simétricos
            if not nodo1 or not nodo2:
                return False
            # si los valores de los nodos no son iguales, devuelve falso ya que no serían simétricos.
            if nodo1.val != nodo2.val:
                return False

            # Añadimos en el orden en el que se comparan, izquierda con derecha y derecha con izquierda
            queue.append(nodo1.left)
            queue.append(nodo2.right)
            queue.append(nodo1.right)
            queue.append(nodo2.left)

        return True
