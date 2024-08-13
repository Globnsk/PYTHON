from time import time

def external (param):
    def deco(func):
        def wrapper(*args):
            sum_time = 0
            for _ in range (param):
                t1 = time()
                res = func(args[0], args[1])
                t2= time()
                sum_time += t2 - t1
            return res, t2 - t1, sum_time
        return wrapper
    return deco

@external (1000000)  #Синтаксический сахар
    
def calc(a, b):
    return a + b

print (calc(2, 3))

#print (external(1000000(calc)(5,8))) # Вариант без сахара

# t1 = time()
# print (func(2, 3))
# t2 = time()
# print (t2 - t1)




