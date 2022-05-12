'''
l = [ x*x for x in range(10000000000000000000000000)]
print(l[0])
print(l[1])
print(l[2])
'''
g = iter(x*x for x in range(10000000000000000000000000))
print(g[0])
print(g[1])
print(g[2])