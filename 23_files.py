file = open('./text.txt')
print(file.read())

# de esta forma abrimos el archivo linia a linia

# print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())


# de estama manera podemos iterar linia a linia y la maquina ya sabra cuando parar, no lo vemos completo

for line in file:
    print(line)
    
#para cerrar el  archivo cuando ya no lo vayamos a utilizar
    
file.close()

# de esta forma tambien podemos abrir un archivo txt sin luego tener que cerrarlo ya qu python lo cierra por si solo.y lo leemos lini a linia.

with open('./text.txt') as file:
    for line in file:
        print(line)

