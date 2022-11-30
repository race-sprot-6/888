def rename(name, ):
    name = [_.replace("su hor", "SU_Hor") for _ in name]

file = open("shtuka.dat", "r")
file_with_lines = file.readlines()[1:267]

allall = []
for line in file_with_lines:
    a = line.split("   ")
    f_st = line.split("   ")[:1]
    t_st = line.split("    ")[1:2]
    tt_st = line.split("    ")[2:3]
    v_st = line.split("    ")[3:4]
    allall.append(f_st+t_st+tt_st+v_st)
    name = []
    lume = []
    for j in range(0, len(allall)):
        name.append(allall[j][0])
        name.append(allall[j][2])
        lume.append(allall[j][3])

name = [_.replace("su hor", "SU_Hor") for _ in name]  #танцы с бубнами ради того, чтобы все su hor, SU Hor и прочие нечисти стали SU_Hor
name = [_.replace("SU Hor", "SU_Hor") for _ in name]
name = [_.replace("RZ Lyr", "RZ_Lyr") for _ in name]
name = [_.replace("rzlyr", "RZ_Lyr") for _ in name]
name = [_.replace("RZLyr", "RZ_Lyr") for _ in name]
name = [_.replace("b", "B") for _ in name]
name = [_.replace("v", "V") for _ in name]
name = [x.strip(" ") for x in name] #удалил пробелы из списка name
lume = [x.strip(" ") for x in lume]
lume = [x.strip("\n") for x in lume]
Obj = []
for j in range(0, len(name)):
    if (j+1)%2 == 1:
        Obj.append(name[j])

filt_SU_Hor = []
for i in range(0, len(name)): #делаем список из фильтров для SU_Hor
    if i%2 == 1 and name[i-1] == name[0]:
        filt_SU_Hor.append(name[i])

filt_RZ_Lyr = []
for i in range(0, len(name)): #делаем список из фильтров для RZ_Lyr
    if i%2 == 1 and name[i-1] == name[462]:
        filt_RZ_Lyr.append(name[i])

filt = []
for i in range(0, len(name)):
    if i%2 == 1:
        filt.append(name[i])

from collections import OrderedDict #убираем дубли, трибли, и тд
OBJ = list(OrderedDict.fromkeys(Obj))

f_SU = list(OrderedDict.fromkeys(filt_SU_Hor))

f_RZ = list(OrderedDict.fromkeys(filt_RZ_Lyr))

print(f"\n \t Объекты: {OBJ} \n \t Фильтры для SU_Hor: {f_SU} \n \t Фильтры для RZ_Lyr: {f_RZ} ")

HJD_SU_Hor_B = []                       #выделяем из списка только даты для SU_Hor и B, а потом светимость для них же
lume_S_B =[]
for i in range(0, len(allall)):
    if Obj[i] == OBJ[0] and filt_SU_Hor[i] == f_SU[0]:
        HJD_SU_Hor_B.append(allall[i][1])
        lume_S_B.append(lume[i])
HJD_SU_Hor_Ic = []
lume_S_Ic = []
for i in range(0, len(allall)):
    if Obj[i] == OBJ[0] and filt_SU_Hor[i] == f_SU[1]:
        HJD_SU_Hor_Ic.append(allall[i][1])
        lume_S_Ic.append(lume[i])
HJD_SU_Hor_V = []
lume_S_V = []
for i in range(0, len(allall)):
    if Obj[i] == OBJ[0] and filt_SU_Hor[i] == f_SU[2]:
        HJD_SU_Hor_V.append(allall[i][1])
        lume_S_V.append(lume[i])
HJD_RZ_Lyr_B = []
lume_R_B = []
for i in range(0, len(allall)):
    if Obj[i] == OBJ[1] and filt[i] == f_RZ[0]:
        HJD_RZ_Lyr_B.append(allall[i][1])
        lume_R_B.append(lume[i])
HJD_RZ_Lyr_V = []
lume_R_V = []
for i in range(0, len(filt)):
    if Obj[i] == OBJ[1] and filt[i] == f_RZ[1]:
        HJD_RZ_Lyr_V.append(allall[i][1])
        lume_R_V.append(lume[i])
list_HJD_SU = []
list_HJD_SU.extend([HJD_SU_Hor_B, HJD_SU_Hor_Ic, HJD_SU_Hor_V])
list_lume_SU = []
list_lume_SU.extend([lume_S_B, lume_S_Ic, lume_S_V])
list_HJD_RZ = []
list_HJD_RZ.extend([HJD_RZ_Lyr_B, HJD_RZ_Lyr_V])
list_lume_RZ = []
list_lume_RZ.extend([lume_R_B, lume_R_V])
i_obj = input("Введите название объекта:" )
i_filt = input("Введите названия фильтров через запятую:" )
i_f = i_filt.split(",")
odin = OBJ[0]
dva = OBJ[1]
if i_obj == odin:
    for i in range(0, len(i_f)):
        for j in range(0, len(f_SU)):
            if i_f[i] == f_SU[j]:
                print(f"\n \t HJD для {f_SU[j]}:{list_HJD_SU[j]} \n \t Magnitude для {f_SU[j]}: {list_lume_SU[j]}")
if i_obj == dva:
    for i in range(0, len(i_f)):
        for j in range(0, len(f_RZ)):
            if i_f[i] == f_RZ[j]:
                print(f"\n \t HJD для {f_RZ[j]}:{list_HJD_RZ[j]} \n \t Magnitude для {f_RZ[j]}: {list_lume_RZ[j]}")