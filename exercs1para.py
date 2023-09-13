import random, math, os


def is_prime(integer):
    for i in range(2, integer // 2):
        if integer % i == 0:
            return False
    return True

#1,2
print(1)
print()
rnd_tznch = random.randint(100, 999)
print(rnd_tznch)
rnd_tznch = str(rnd_tznch)
rnd_tznch_sum = 0
for symb in rnd_tznch:
    rnd_tznch_sum += int(symb)
print(rnd_tznch_sum)
#3
print(3)
print()
radius = int(input())
print(f"S={4 * math.pi * radius**2}\nV={(4/3)*math.pi*radius**3}\nwith radius={radius}")
#4
print(4)
print()
rnd_year = random.randint(1, 3000)
print(f"year={rnd_year}")
if rnd_year % 4 == 0 and rnd_year % 100 != 0:
    print("this year is leap")
else:
    print("this year is not leap")
#5
print(5)
print()
rnd_range = random.randint(1, 10000)
prime_ns = []
for i in range(1, rnd_range):
    if is_prime(i):
        prime_ns.append(i)
print(prime_ns)
#6
print(6)
print()
X = random.randint(1000, 10000)
Y = random.randint(1, 10)
print(f"X={X}, Y={Y}")
for year in range(Y):
    X += X * 0.1
print(X)
#7
print(6)
print()
dirs = ["C:\\Users\\m.unzhakov\\Desktop\\python"]

while len(dirs) != 0:
    cur_dir = dirs.pop()
    list_of_files = os.listdir(cur_dir)
    folder_name = cur_dir.split('\\')[-1]
    print(f"folder {folder_name} contains this files: {list_of_files}")
    for file in list_of_files:
        path = cur_dir + "\\" + file
        if os.path.isdir(path):
            dirs.append(path)