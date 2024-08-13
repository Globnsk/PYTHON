# def func(**kwargs): # Неограниченное кол-во ПОИМЕНОВАННЫХ аргументов
#     return   sum(kwargs.values())

# s = func(a=100, b=200, c=300, d=700)
# print (s)

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() |