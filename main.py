file = open("chisla.dat", "r")
file_with_lines = file.readlines()
for line in file_with_lines:
    chisla = line.split(',')
    for k in range(0,len(chisla)-1):
        for i in range(0,len(chisla)-1):
            if int(chisla[i]) < int(chisla[i+1]):
                chisla[i] = chisla[i]
            else:
                t = chisla[i]
                chisla[i] = chisla[i+1]
                chisla[i+1] = t
print(chisla)

my_var = ['Ivan', 'Rinat', 'Olga', 'Kira']

# в новый список записываем элементы начального списка, измененные
# с помощью replace
new_list = [_.replace("i", "A", 1) for _ in my_var]
print(new_list)
# Вывод:

['Ivan', 'RAnat', 'Olga', 'KAra']