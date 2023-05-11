cars = {}

def add():
    number = input("введите номер машины: ")
    cars[number] = 0

def exit():
    number = input("введите номер машины, которую хотите забрать: ")
    for key, val in cars.items():
        if key != number:
            val += 1
        else:
            cars.pop(key)
 
