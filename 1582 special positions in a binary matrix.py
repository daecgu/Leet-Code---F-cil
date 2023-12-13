class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if self.solo_en_fila(i,j,mat) and self.solo_en_columna(i,j,mat):
                    count += 1
        return count



    def unos_en_fila(self, fila: int,  mat: list[list[int]]) -> int:
        count = 0
        for each in mat[fila]:
            if each == 1:
                count += 1
        return count

    def unos_en_columna(self,columna: int, mat: list[list[int]]) -> int:
        count =0
        for fila in mat:
            if fila[columna] == 1:
                count += 1
        return count

    def solo_en_fila(self, fila: int, columna: int, mat: list[list[int]]) -> int:
        if mat[fila][columna] == 0 or self.unos_en_fila(fila, mat) > 1:
            return False
        return True

    def solo_en_columna(self, fila: int, columna: int, mat: list[list[int]]) -> int:
        if mat[fila][columna] == 0 or self.unos_en_columna(columna, mat) > 1:
            return False
        return True