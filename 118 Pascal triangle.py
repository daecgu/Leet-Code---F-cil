def generate(numRows: int):
    def generar_fila(numero_fila_actual):
        """
        Esta función lo que realiza es generar una fila a partir de la fila anterior.
        Es necesario pasarle el número de fila actual.
        Lo primero que hace es meter en la fila el 1 inicial.
        Luego a partir de la segunda posición calcula el valor para el sitio actual y lo agrega a la fila
        """
        result = [1]
        for position in range(1, numero_fila_actual - 1):
            calculo = resultado[numero_fila_actual - 2][position] + resultado[numero_fila_actual - 2][position - 1]
            result.append(calculo)
        result.append(1)
        return result
    # si el número de filas es 1 se da el resultado
    if numRows == 1:
        resultado = [[1]]
        return resultado
    # si el número de filas es 2 se devuelve el resultado
    elif numRows == 2:
        return [[1],[1,1]]
    # si el número de filas es superior a 3 se generará una nueva fila partiendo con la base del triangulo de dos filas.
    else:
        resultado = [[1],[1,1]]
        for each in range(3, numRows+1):
            resultado.append(generar_fila(each))

    return resultado

print(generate(10))

