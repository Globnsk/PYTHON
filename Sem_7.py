#TASK 47
# values = [1, 34, 11, 78, 63, 44, 707, 17]
# transformation = lambda x: x
# transformed_values = list(map(transformation, values))
# if transformed_values == values:
#     print ('OK')
# else:
#     print("False")

#TASK 49

# from math import pi
# def find_fartherst_orbit(list_of_orbits):
#     list_1 = [i for i in list_of_orbits if i[0]!=i[1]]
#     list_s = [(pi*i[0]*i[1]) for i in list_1]
#     max_s = list_s.index(max(list_s))
#     return list_1 [max_s]


# orbits = [(6,4), (7,7), (2,8), (9,6), (8,4)]
# print (*find_fartherst_orbit(orbits))
# #find_fartherst_orbit(orbits)
    
#Task 51

def same_by (charachteristic, object):
    result = True
    list_1 = [charachteristic(x) for x in object]
    for i in range (len(list_1)-1):
        if list_1[i]!=list_1[i+1]:
            result = False
    return result

value = [0,3,12,8,6,56]
if same_by (lambda x: x%2, value):
    print ('SAME')
else:
    print ('DIFFERENT')
