file = open("shtuka.dat", "r")
file_with_lines = file.readlines()[1:267]

obj = []
filt = []
for line in file_with_lines:
    a = line.split("   ")
    f_st = line.split("   ")[:1]
    t_st = line.split("    ")[2:3]
    obj.append(f_st+t_st)
    name = []
    Obj = []
    for j in range(0, len(obj)):
        name.append(obj[j][0])
        name.append(obj[j][1])
        #if obj[j][0] = obj[j+1][0]:
    for j in range(0, len(obj)):
        Obj.append(obj[j][0])

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

filt_RZ_Lyr = []
for i in range(232, len(name)): #делаем список из фильтров для RZ_Lyr
    if i%2 == 1:
        filt_RZ_Lyr.append(name[i])

filt_RZ_Lyr = [_.replace("b", "B") for _ in filt_RZ_Lyr]
filt_RZ_Lyr = [_.replace("v", "V") for _ in filt_RZ_Lyr]

from collections import OrderedDict #убираем дубли, трибли, и тд
k = list(OrderedDict.fromkeys(Obj))

f_SU = list(OrderedDict.fromkeys(filt_SU_Hor))

f_RZ = list(OrderedDict.fromkeys(filt_RZ_Lyr))

print(f"\n \t Объекты: {k} \n \t Фильтры для SU_Hor: {f_SU} \n \t Фильтры для RZ_Lyr: {f_RZ} ")
