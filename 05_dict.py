# llave multiplicado * 2
dict = {}
for i in range(1,5):
    dict[i]= i * 2
    
print(dict)

dict_2 = {i:i * 2 for i in range(1,5)}
print(dict_2)


import random
countries = ['col', 'mex', 'bol','pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
    
    print(population) 
    
population = {country: random.randint(1,100) for country in countries}
print(population)

names = ['nico','zule','santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip (names , ages)}
print(new_dict)


# otra forma de hacer la dictionary comprehension entre 2 listas formando un diccionario

new_dict_2 = {names[i]:ages[i] for i in range(len(names))}
print(new_dict_2)

