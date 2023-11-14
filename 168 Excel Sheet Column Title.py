import string


def converttotitle(columnNumber: int) -> str:
    respuesta = ''
    letras = string.ascii_uppercase

    while columnNumber > 0:
        # Ajustar para el desbordamiento de 'Z'
        modulo = (columnNumber - 1) % 26
        respuesta = letras[modulo] + respuesta
        columnNumber = (columnNumber - 1) // 26

    return respuesta


print(converttotitle(702))
