import random

value = random.randint(10, 15)
s = []

for i in range(value):
    s.append(random.randint(0, 99))

def merge_two_list(a, b):
    c = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c += a[i:]
    elif j<len(b):
        c += b[j:]
    return c

def merge_sort(s):
    if len(s)==1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)

print(merge_sort(s))