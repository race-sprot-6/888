# file = open("chisla.dat", "r")
# #"r" - чтение, "w" - запись, "a" - дозапись, "x" - ..., "+" - чтение и запись
# #print(file.readlines())
# file_with_lines = file.readlines()
# for line in file_with_lines:
#     a = line.split("y")
import scipy

a = [1,3,4,0]
k = a.index()
b = max(a)
print(b)





#Лекция 5.
#Для задания функции используем слово def nameoffunc (): в скобках параметры функции. В пробеле набор команд.
def summ():
    a = 6
    b = 7
    c = a+b
    print(f"summ = {c}")
#summ() #вызываем функцию



def print_max(d, e): #принимает значения параметров d и e
    if d > e:
        print(f"{d} is max")
    elif e > d:
        print(f"{e} is max")
    else:
        print(f"{d} = {e}")

#print_max(4, 5) #прямая передача аргументов

def summ2(*numbers):
    s = 0
    for i in numbers:
        s += i #s = s +i
    print(s)
#summ2(2, 5, 9, 10)


#Лекция
def some_func_2():
    global p
    p = 20
    print(f" {p} ")
p = 50
some_func_2()
p = 2
print(p)

a = 55.44
b = str(a)
print(b)