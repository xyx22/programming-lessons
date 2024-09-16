my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

number = 0
while number < len(my_list):
    element = my_list[number]
    number += 1
    if element == 0:
        continue
    elif element < 0:
        break
    print(element) # чтобы остановиться до первого минула

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

number = 0
while number < len(my_list):
    element = my_list[number]
    number += 1
    if element == 0:
        continue
    elif element < 0:
        continue
    print(element) # чтобы перебрать и выбрать только положительные 