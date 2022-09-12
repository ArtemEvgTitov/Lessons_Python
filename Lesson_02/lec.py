# import func as f
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)  # Разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# print(f.f(1))


# def new_string(symbol, count=3):
#     return symbol*count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))  # a1


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]


# a = (3 ,4) # Кортеж - неизменяемый список
# print(a)
# print(a[0])
# print(a[-1])

# dictionary = {}
# dictionary = \
#     {
#         'left': '<-',
#         'right': '->'
#     }
# #print(dictionary['left']) # <-

# for k in dictionary.keys():
#     print(k)
# for k in dictionary.values():
#     print(k)

colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')  # ok
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { }
print(colors)  # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
