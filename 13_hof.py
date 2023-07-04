def increment(x):
  return x + 1

def high_ord_func(x, func):
  return x + func(x)
result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

# usando las lambdas

increment_v2 =  lambda x: x + 1

high_ord_func_v2 = lambda x, func: x + func(x) 
result = high_ord_func_v2(2,increment_v2  )
print(result)
# una vez definida la high_ord_func esta funcion increment_v2 
# podemos de estar cambiandola muy dinamicamente sin necesidad de definirla o asignarla a una variable como  tal
result = high_ord_func_v2(2, lambda x: x + 2 )
print(result)
# change in the lambda function
result = high_ord_func_v2(2, lambda x: x * 5 )
print(result)