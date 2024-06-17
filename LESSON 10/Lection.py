# def calc1(a):
#     return a+a

# def calc2(a):
#     return a*a

# def math(op,x,y): 
#     print(op(x,y))

# math(lambda a,b: a+b,5,45)

# data=[1,2,3,5,8,15,23,38]
# res=list()
# for i in data:
#     if i%2==0:
#         res.append((i,i**2))
# print (res)

# THE NEXT

# def select (f,col):
#     return [f(x) for x in col]

# def where (f,col):
#     return [x for x in col if f(x)]

# data=[1,2,3,5,8,15,23,38]
# res=select(int,data)
# print(res)
# res=where(lambda x: x%2==0, res)
# res=list(select(lambda x: (x,x**2), res))
# print(res)

#THE NEXT (MAP)

# list_1=[x for x in range(1,21)]
# print(list_1)
# list_1=list(map(lambda x: x+10, list_1))
# print(list_1)

#THE NEXT
#Преобразовать list строк в list чисел

# data = '1 23 43 70 64 77 91 345 67'
# data = list(map(int, data.split()))
# print (data)

#THE NEXT (filter function)

# data = [5, 10, 15, 115, 27, 14, 35, 89, 455]
# res = list(filter(lambda x: x % 10 ==  5, data))
# print (res)

#THE NEXT (FILES)

# colors = ['red', 'green', 'blue']
# data = open ('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open ('file.txt', 'w') as data:
#     data.write('Line_1\n')
#     data.write('Line_3\n')
# print (1)

path = 'file.txt'
data = open ('file.txt','r' )
for line in data:
    print (line)
data.close








