file = open("shtuka.dat", "r")
file_with_lines = file.readlines()
name = []
for line in file_with_lines:
    st = line.split('  ')
    first_st = int(line.split()[:1])
    name.append(first_st)
first_set = set(name)
print('first_set =', first_st)
    #print(line.split()[:2], line.split()[3:4])
#print(first_st)