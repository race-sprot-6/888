file = open("shtuka.dat", "r")
file_with_lines = file.readlines()[1:267]
name = []
for line in file_with_lines:
    a = line.split("    ")
    f_st = line.split("    ")[:1]
    t_st = line.split("    ")[2:3]
    print(f_st)
    print(t_st)
    name.append(f_st+t_st)
    #name.append(t_st)
from itertools import chain
spisok = list(map(str, chain.from_iterable(name)))
from collections import OrderedDict
k = list(OrderedDict.fromkeys(spisok))
#first_set = set(spisok)
print(f"\n \t {k} \n")