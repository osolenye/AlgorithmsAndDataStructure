import json


with open('trains.txt') as f:
    data = f.read()


trains = json.loads(data)

def add():
    num = int(input("введите номер поезда: "))
    station = input("введите станцию назначения: ")
    time = input("введите время отправления: ")
    trains[num] = [station, time]

    #записывает в файл наш словарь
    with open('trains.txt', 'w') as trains_txt:
        trains_txt.write(json.dumps(trains))


        


def show_trains():
    print(trains)

def trains_by_number():
    num = int(input("введите номер поезда, чтобы получить о нем информацию: "))
    print(trains[num])

def trains_by_station():
    station = input("введите название станции: ")
    for key, val in trains.items():
        if val[0] == station:
            print(key, val)
            


print('список команд для работы с системой: \n'
        'введите "add" для того, чтобы добавить информацию о новом поезде \n'
        'введите "show" для того, чтобы получить информацию о всех поездах \n'
        'введите "number" для того, чтобы получить информацию о поезде по номеру \n'
        'введите "station" для того, чтобы получить информацию и поездах, едущих на конкретную станцию \n'
        'введите "stop", чтобы завершить программу.'
        )


while True:

    #подгружает из файла наш словарь
    with open('trains.txt') as f:
        data = f.read()

    trains = json.loads(data)

    a = input()
    if a == "add":
        add()
    elif a == "show":
        show_trains()
    elif a == "number":
        trains_by_number()
    elif a == "station":
        trains_by_station()
    elif a == "stop":
        break
    else:
        print("невиданная команда, проверьте правильность введенной команды")

