items = [
    
    {
       
       'product': 'camisa',
       'price': 100
    },
    {
       'product': 'pantalones',
       'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
        
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)


# añadimos uma tasa de impuesto a items, como lambda solo se tiene que hacer en una sola linia ,
# y seran mas , tenemos que crear una nueva funcion para luego hacer el map.

def add_taxes(item):
    item['taxes']= item['price'] * .19
    return item 

# hacemos el map

new_items = list(map(add_taxes,items))
print('New list')
print(new_items)
print('old list')
print(items)

def multiply_numbers(numbers):
   
    return list(map(lambda a: a * 2, numbers))
    

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)