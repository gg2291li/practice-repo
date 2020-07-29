a = [[1, 2], [2, 3]]
b = [[2, 3], [4, 5]]
c = a + b
d = c[:]
d.insert(4, 5)
print(c)
print(d)