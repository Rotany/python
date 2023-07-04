import functools

numbers = [1, 2, 3, 4]
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)


# vamos abrilo en una función: vamos a escribir la misma lambda function

def  accum(counter, item):
  print('counter =>' ,counter)
  print('item =>' ,item)
  return counter + item

result = functools.reduce(accum, numbers)
print(result)