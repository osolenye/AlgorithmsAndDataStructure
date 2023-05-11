numbers = [2, 18, 5, 7, 2, 32, 6, 9, 4, 8, 9, 12, 14, 14]

my_dict = {}
for n in numbers:
    if n not in my_dict:
        my_dict[n] = numbers.count(n)

print(my_dict)