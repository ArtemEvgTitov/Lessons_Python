print('Hello world!')

# типы данных и переменная
# int, float, boolean, str, list, None

value = None
a = 123
b = 1.23
print(type(a))
print(b)
value = 12345
print(value)
s = 'hello world'
print(s)

print(a, '-', b, '-', s)
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a, b, s))

f = True

list = [1, True, 3.21, 'Hello world']
print(list)

print('Введите а: ')
a = int(input())

# Арифметические операции
# +, -, *, /, %, //, **

a = 1.3
b = 3
c = round(a * b, 3)
print(c)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# is, is not, in, not in
# gen

f = [1, 2, 3, 4]
print(2 in f)
# is_odd = f[0] % 2 == 0
is_odd = not f[0] % 2
print(is_odd)

# Управляющие конструкции
# if, if-else, while, for

for i in 1, 2, 3, 4, 5:
    print(i**2)

list - [1, 2, 3, 45, 3]
for i in list:
    print(i**2)

for i in range(1, 10, 2):
    print(i)

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент
