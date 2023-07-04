def suma( a = 5, b = 20):
    return a+b
print (suma() * 2)

print (suma(1, 2))
print(suma (1, 2) * 2)

print(suma(b= 10))
print(suma(1))

def resta(a = 9, b = 40, c = 5):
    return a+b-c

print(resta() * 5)
print(resta(1, 8, 50))
print(resta(b= 4))
print(resta(10, 20, 5) /5)


def div(a = 40, b = 10, c = 5):
    return a+b/c
print(div() * 5)
print(div(20, 50,2)*6)
print(div(c = 5))
print(div(1))


def mult(a = 8, b = 50):
    return a*b

print(mult()**2)
print(mult(8, 50) / 4)
print(mult(100, 50) +50)
print(mult(50)*8)