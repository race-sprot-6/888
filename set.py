file = open("shtuka.dat", "r")
file_with_lines = file.readlines()[1:267]

allall = []
#filt = []
for line in file_with_lines:
    a = line.split("   ")
    f_st = line.split("   ")[:1]
    t_st = line.split("    ")[1:2]
    tt_st = line.split("    ")[2:3]
    v_st = line.split("    ")[3:4]
    allall.append(f_st+t_st+tt_st+v_st)
    name = []
    Obj = []
    for j in range(0, len(allall)):
        name.append(allall[j][0])
        name.append(allall[j][2])
        #if obj[j][0] = obj[j+1][0]:
    for j in range(0, len(allall)):
        Obj.append(allall[j][0])

Obj = [_.replace("su hor", "SU_Hor") for _ in Obj]  #танцы с бубнами ради того, чтобы все su hor, SU Hor и прочие нечисти стали SU_Hor
Obj = [_.replace("SU Hor", "SU_Hor") for _ in Obj]
Obj = [_.replace("RZ Lyr", "RZ_Lyr") for _ in Obj]
Obj = [_.replace("rzlyr", "RZ_Lyr") for _ in Obj]
Obj = [_.replace("RZLyr", "RZ_Lyr") for _ in Obj]


filt_SU_Hor = []
for i in range(0, 231): #делаем список из фильтров для SU_Hor
    if i%2 == 1:
        filt_SU_Hor.append(name[i])

filt_SU_Hor = [_.replace("b", "B") for _ in filt_SU_Hor]
filt_SU_Hor = [_.replace("v", "V") for _ in filt_SU_Hor]

filt_SU_Hor = [x.strip(" ") for x in filt_SU_Hor] #удалил пробелы из списка filt_SU_Hor

filt_RZ_Lyr = []
for i in range(462, len(name)): #делаем список из фильтров для RZ_Lyr
    if i%2 == 1:
        filt_RZ_Lyr.append(name[i])

filt_RZ_Lyr = [_.replace("b", "B") for _ in filt_RZ_Lyr]
filt_RZ_Lyr = [_.replace("v", "V") for _ in filt_RZ_Lyr]

filt_RZ_Lyr = [x.strip(" ") for x in filt_RZ_Lyr] #удалил пробелы из списка filt_RZ_Lyr

from collections import OrderedDict #убираем дубли, трибли, и тд
OBJ = list(OrderedDict.fromkeys(Obj))

f_SU = list(OrderedDict.fromkeys(filt_SU_Hor))

f_RZ = list(OrderedDict.fromkeys(filt_RZ_Lyr))

print(f"\n \t Объекты: {OBJ} \n \t Фильтры для SU_Hor: {f_SU} \n \t Фильтры для RZ_Lyr: {f_RZ} ")

HJD_SU_Hor = []                       #выделяем из списка только даты для SU_Hor, а потом и для RZ_Lyr
for i in range(0, len(allall)):
    if Obj[i] == OBJ[0]:
        HJD_SU_Hor.append(allall[i][1])
HJD_RZ_Lyr = []
for i in range(0, len(allall)):
    if Obj[i] == OBJ[1]:
        HJD_RZ_Lyr.append(allall[i][1])
#print(HJD_SU_Hor)
#print(HJD_RZ_Lyr)

HJD_filt_SU_Hor = []
for i in range(0, len(filt_SU_Hor)):
    if filt_SU_Hor[i] == f_SU[0]:
        HJD_filt_SU_Hor.append(allall[i][1])

HJD_filt_RZ_Lyr = []
for i in range(0, len(HJD_RZ_Lyr)):
    if filt_RZ_Lyr[i] == f_RZ[0]:
        HJD_filt_RZ_Lyr.append(HJD_RZ_Lyr[i])
print(HJD_filt_SU_Hor)
print(HJD_filt_RZ_Lyr)


