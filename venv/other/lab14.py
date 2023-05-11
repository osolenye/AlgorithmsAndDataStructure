students = {}
n = int(input())

for i in range(n):
    surname, major, group = input().split()
    if major not in students:
        students[major] = []
    students[major].append(surname)

search_major = input().strip()

if search_major in students:
    print(",".join(students[search_major]))
else:
    print("Проверьте запрос")
