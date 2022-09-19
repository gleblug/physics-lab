from time import time

start_value = int(input("Start value: "))
k = 1
exp = []

start_time = time()

inp = input()
exp.append((0, start_value))

while inp != 'exit':
    exp.append((round(time() - start_time, 3), inp))
    inp = input()
    k += 1

print("time,voltage")

for e in exp:
    print(f"{e[0]},{e[1]}")
