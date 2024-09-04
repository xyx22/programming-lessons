my_dict = {"Олег": 2002, "Иван": 2002}
print(my_dict)
print(my_dict.get("Олег"))
print(my_dict.get("Никита"))
my_dict = {"Олег": 2002, "Иван": 2002}
print(my_dict)
my_dict["Макс"]= 1999 #
print(my_dict)
my_dict.update({"Инна": 1998, "Артур" : 1999})
print(my_dict)
a = my_dict.pop("Олег", "Инна") # не получается больше одного
print(a)
#del my_dict["Олег"]
print(my_dict)
# Множество
my_set = {11, 2, 30, 5, 2, "String", "Урбан", (11, 2, 30)}
print(my_set)
print(my_set.add(540))
print(my_set.add(200))
print(my_set.add(200))
print(my_set)
print(my_set.discard(200))
print(my_set)
