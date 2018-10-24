a = [1, 2, 3, 4, 5, 6, 7]

print(a)
a_mul = list(map(str,a))
print(a_mul)

try:
   print(sum(a_mul))
except Exception as e:
    print(e,e.args)
