from numpy import stack, array, reshape, append, insert

a = array([
    ['Mon',18,20,22,17], 
    ['Tue',11,18,21,18],
    ['Wed',15,21,20,19],
    ['Thu',11,20,22,21],
    ['Fri',18,17,23,22], 
    ['Sat',12,22,20,18],
    ['Sun',13,15,19,16]
    ]) 
"""
print(a.shape)

print(a.size)
"""
m = reshape(a, (7, 5))

print(m[2])

print(m[4][3])

add = append(m, [["Base", 1, 2, 3, 4]], 0)

#print(add)

add_c = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)

print(add_c)