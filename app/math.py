def suma( a = 5, b = 20):
    return a+b
print (suma() * 2)

print( suma(1, 2))
print( suma (1, 2) * 2)

print(suma(b= 10))
print(suma(1))

def resta(a = 40, b = 10):
    return a-b

print(resta() * 5)
print(resta(5, 8))
print(resta(b= 4))
print(resta(10, 20) /5)


def div(a = 40, b = 5 ):
    try:
      return a/b  
      
    except ZeroDivisionError as error:
       raise  Exception ('que pasa esto es un error')
    
print(div() * 5)
print(div(20, 50)*6)
print(div(b = 2))

  
 
numbers = [1, 2, 3, 5, 6]  
def multiplicar_array_por_dos(lista): 
    datos=[]
    for number in lista:
        print(number * 2)
        datos.append(number*2)
    return datos
print(multiplicar_array_por_dos(lista = numbers))
 

def mult(a = 8, b = 50):
    return a*b

print(mult()**2)
print(mult(8, 50) / 4)
print(mult(100, 50) +50)
print(mult(50))
print(mult(b=0))
print(div(b=0))