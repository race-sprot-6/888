# ############# 1
# #чтобы находил коэффициенты а, б методом крамера.
import numpy as np
# X = [1, 2, 3, 4, 5]
# Y = [3, 5, 7, 9, 11]
# n = len(X)
#
# summx, summxy, summy, summx2 = 0, 0, 0, 0
# for i in range(0, n):
#     summxy += (X[i] * Y[i])
#     summx += X[i]
#     summy += Y[i]
#     summx2 += X[i]*X[i]
#
# a = (n*summxy - summx*summy)/(n*summx2-(summx)*(summx))
# b = 1/n * summy - a * (summx/n)
# print(a, b)


############# 2


#так. ща поступает матрица в код, например
mini_mas = np.array([[2.0, 5.0, 7.0],
                     [6.0, 3.0, 4.0],
                     [5.0, -2.0, -3.0]])
maxi_mas = np.zeros((len(mini_mas), 2*len(mini_mas)),dtype=float)
for i in range(len(mini_mas)):
    for j in range(2*len(mini_mas)):
        if j>=len(mini_mas):
            if i == j-len(mini_mas):
                maxi_mas[i][j]=1
        else:
            maxi_mas[i][j]=mini_mas[i][j]
print("расширенная матрица = ", maxi_mas)
mas = maxi_mas

#_____________ Преобразование матрицы____________
#_____________сверху вниз__________
for i in range (0, len(mas)): #заходим в цикл по строкам
    a = mas[i][i] #сохраняем ii элемент, на него поделим потом
    for j in range (2*len(mas)): #в цикл по столбцам. их колво = 2*колво строк
        mas[i][j] = mas[i][j]/a #чтобы ii элемент стал единичным
    # print(mas)
    for k in range (i+1, len(mas)): #переходим на сл строку
        b = mas[k][i]
        for j in range(2*len(mas)):
            mas[k][j]+=mas[i][j]*(-1)*b #вычитаем предыдущую строку, чтобы занулить (i+1,i) элемент
    # print(mas) #ура, пришли к единицам по гл диагонали и нулям ниже нее

#_____снизу вверх_____
for i in range (len(mas)-1,0,-1): #с нижней строки движемся вверх
    for k in range (i-1, -1, -1): #начинаем с последнего столбца влево
        b = mas[k][i]
        for j in range(2*len(mas)):
            mas[k][j]-=mas[i][j]*b #
print(mas) #len(mas) = 3

rev_mas = np.zeros((len(mini_mas), len(mini_mas)),dtype=float)
# for k in range(0, len(mas)):
for i in range (0,len(mas)):
    for j in range (0, len(mas)*2):
        if j>=len(mas):
            rev_mas[i][j-len(mas)] = mas[i][j]
print(rev_mas)