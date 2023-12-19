from typing import List
import math

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        resultado = []
        for i in range(0,m):
            resultado.append([])
            for j in range(0,n):
                resultado[i].append(self.avg_filtro(img, i, j))

        return resultado
    def avg_filtro(self, img, i,j) -> int:
        m = len(img)
        n = len(img[0])
        suma = 0
        cuenta = 0
        for z in range(-1, 2):
            if i+z >= 0 and i+z < m:
                for y in range(-1, 2):
                    if j+y >= 0 and j+y < n:
                        suma = suma + img[i+z][j+y]
                        cuenta += 1
        return math.floor(suma/cuenta)
