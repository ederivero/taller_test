def sumar(num1, num2):
    if (isinstance(num1, float) or isinstance(num1, int)) and (isinstance(num2, float) or isinstance(num2, int)):
        return num1 + num2
    else:
        raise TypeError('Los parametros debe ser numericos')

