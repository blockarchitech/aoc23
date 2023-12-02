import re
import time

start_time = time.time()
lines = open("1/input.txt", "r").readlines()

find = lambda s: re.findall(r"\d+", s)
split = lambda l: [i for i in "".join(l)]
combine = lambda l: l[0] + l[-1]
values = []

for line in lines:
    values.append(int(combine(split(find(line)))))

print(sum(values))
print("--- %s seconds ---" % (time.time() - start_time))
