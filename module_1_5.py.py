immutable_var = 15, 72, 64, 'Один'
print(immutable_var)
#tuple[0] = 20 # не поддерживает изменение по элементу но если
mutable_list = [15], 72, [15], ['Один']
mutable_list[2][0] = 20 #ТОГДА ПОЛУЧАЕТСЯ
mutable_list[0][0] = 20
mutable_list[3][0] = 'Одиннадцать'
print(mutable_list)
#mutable_list[0][0] = 'Одиннадцать'