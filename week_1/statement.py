if True:
    print('It is True!')
# for loop
my_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_iterable:
    if number % 2 == 0:
        print(number)
    else:
        print("Odd")
# dictionary
d = {"k1": 1, "k2": 2, "k3": 3}
for key, value in d.items():
    print(value)
# tuple
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (a, b) in my_list:
    print(b)

# while loop
x = 0

while x < 5:
    x += 1
    print(f'Number is {x}')
