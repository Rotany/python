numbers = []
for element in range(1, 11):
    numbers.append(element)
    print(numbers)
    # multiplicando por 2 el elemnet
    numbers = []
    for i in range(1,11):
        numbers.append(i*2)
        print(numbers)
        
    # Usando la formula List Comprehensions y usando una condicion
    
    
    numbers_v2 = [i*2 for i in range(1,11)if i %2==0]
    print(numbers_v2)
    
    
    