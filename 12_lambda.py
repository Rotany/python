def increment(x):
    return x +1
result = increment(10)
print(11)

# haciendo un lambda: el landa lleva los datos de entrada y de salida

increment_v2 = lambda x :  x + 1
result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'My name is{name.title()} {last_name.title()}'

text = full_name(' Tanya', 'Vitonera Gastiabur')

print(text)

my_data = lambda name, last_name, age, birthdate: f'My data is {name.title()} {last_name.title()} {age.title()} {birthdate.title()}'
text = my_data(' tanya', ' vitonera gastiabur','45 años',  '04/03/78  naci en ecuador')
print(text)