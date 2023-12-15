from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        diccionario = dict(paths)
        for each in diccionario.values():
            if not each in diccionario:
                return each

    def convertir_a_diccionario(self, paths: List[List[str]]) -> dict:
        return dict(paths)

