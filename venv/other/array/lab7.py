array = []
counter = 0

for i in range (1, 8):
    array.append(int(input(f"введите продажи магазина за {i} день недели: ")))
for i in range (0, 7):
    counter += array[i]
print(f'общий объем продаж магазина за неделю составил: {counter}')