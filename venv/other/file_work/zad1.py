import os

# print(os.path.basename(r'venv/file_work/txt1.txt'))
print("первое задание")
with open("txt1.txt", "r", encoding="utf-8") as f:
    info = f.readline()
    print(info)
    info = f.readline()
    print(info)
    info = f.readline()
    print(info)

# print("zadanie 2")
# filename = input("Введите имя файла: ")
# num_lines = 0
# num_words = 0
# num_chars = 0
# with open(filename, 'r') as file:
#     for line in file:
#         words = line.split() #разбивает строку на слова
#         num_lines += 1 # инкременция counter строк, каждую итерацию берет новую строку
#         num_words += len(words) # добавляем к счетчику слов длину массива слов
#         num_chars += sum(len(word) for word in words) # добавляем к кол-ву символов колво символов
#
# num_chars = num_chars - (num_words - 1)
#
# print("Количество строк:", num_lines)
# print("Количество слов:", num_words)
# print("Количество символов", num_chars)

print("задание 3")
with open("txt1.txt", "r", encoding="utf-8") as f:
    words = f.read().replace('"', '').split()
    result = [w for w in words if len(w) == len(max(words, key=len))]
print(result)


print("задание 4")
with open('fruit.txt', 'r', encoding='utf-8') as file:
    result = {}
    for line in file:
        words = line.strip().lower().split()
        for w in words:
            result[w] = result.get(w, 0) + 1
print(f'Названия этих фруктов встречаются в тексте:')
for k, v in result.items():
    print(f'"{k}" - {v} раз(а)')

print('задание 5')
with open("first.txt", "r") as f1, open("second.txt", "r") as f2:
    names = f1.readlines()
    positions = f2.readlines()

    names = [name.strip() for name in names]
    positions = [position.strip() for position in positions]

    employees = list(zip(names, positions))

    for employee in employees:
        print(f"Сотрудник {employee[0]}, должность - {employee[1]}")

print("задание 6")
alpha = [i for i in range(ord('а'), ord('я') + 1)]
alpha.insert(6, 1105)
with open('alphabet.txt', 'w', encoding='utf-8') as file:
    for i in alpha:
        file.write(chr(i).upper() + chr(i) + '\n')
with open('alphabet.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

print("задание 7")
income, outcome = 0, 0
with open('income.txt', 'r', encoding='utf-8') as file1, \
open('outcome.txt', 'r', encoding='utf-8') as file2:
    for line in file1:
        num = line.strip()[3:]
        income += int(num)

    for line in file2:
        num = line.strip()[4:]
        outcome += int(num)
print(f'Прибыль за прошлый месяц: {income - outcome} RUB')

print('задание 8')
result = {}
with open('grades.txt', 'r', encoding='utf-8') as file1:
    for line in file1:
        l = line.strip().split()
        grades = [int(i) for i in l[-4:]]
        aver_grade = sum(grades) / len(grades)
        if aver_grade >= 4.5:
            result[l[0] + ' ' + l[1]] = aver_grade
for student, aver_grade in result.items():
    print(f'{student}, средний балл: {aver_grade:.2f}')

print("задание 9")
translit = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n',
     'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh',
     'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
     'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N',
     'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh',
     'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'}
filename = input()
with open(filename, 'r', encoding='utf-8') as source, open('result.txt', 'w', encoding='utf-8') as tr_result:
    for l in source.read():
        trans = translit.get(l.lower(), l)
        tr_result.write(trans if l.islower() else trans.capitalize())
with open("result.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

print("задание 10")
with open('crm_log.txt', encoding='utf-8') as file_input, \
     open('best_employees.txt', 'w', encoding='utf-8') as file_output:

    for line in file_input:
        start, end = [int(h) * 60 + int(m) for t in line.split(', ')[1:] for h, m in [t.split(':')]]
        if end - start > 240:
            file_output.write(line.split(', ')[0] + '\n')

with open("best_employees.txt", "r", encoding='utf-8') as f:
    text = f.read()
    print(text)