def find_volume(lenght, width,depth):
    return lenght * width * depth
result = find_volume( 10,20,3)
print(result)

# pero en python tambien podemos definir valores por defecto

def find_volume(lenght= 1, width= 1,depth= 1):
    return lenght * width * depth
result = find_volume(width= 10 )
print(result)

# en python podemor retornar mas de una funcion

def find_volume(lenght= 1, width= 1,depth= 1):
    return lenght * width * depth, width, 'hola'
result = find_volume(width= 10 )
print(result)

# como el resultado es una tupla, solo quiero un valor, que me envie la posicion 0


def find_volume(lenght= 1, width= 1,depth= 1):
    return lenght * width * depth, width, 'hola'
result = find_volume(width= 10 )
print(result[0])

#tambien podriamos hacer solo con una coma en el resultado poner las variable que quiero que me retorne


def find_volume(lenght= 1, width= 1,depth= 1):
    return lenght * width * depth, width, 'hola'
result, width, text = find_volume(width= 10 )
print(result)
print(width)
print(text)
