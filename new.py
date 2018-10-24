a = [15, 19.5, 'hello', True]
print(a)
print(a[1])

a[1] = 'word'
print(a)

print(type(a[-1]))
print(type(a[len(a)-1]))

print(dir(a))
a.append('one')
print(a)