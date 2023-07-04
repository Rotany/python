numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers :
   numbers_v2.append(i * 2)
   
   
   
   # Haciendo uso del Map y Lambda function
   
   numbers_v3 = list(map(lambda i: i*2, numbers))
   

print(numbers)
print(numbers_v2)
print(numbers_v3)


# en este codigo hacemos un map y lambda function de sumando 2 listas, pero nos noarroja como resultado solo una lista y la más corta


numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)