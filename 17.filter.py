numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x:x % 2 == 0, numbers))
print(new_numbers)
# filter crea una lista con los elementos que cumple una condición ,pero sin alterar la lista anterior.
#lo contrario de map .
