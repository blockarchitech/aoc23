import time
from tqdm import tqdm

starttime = time.time()
lines = open("6/input.txt").readlines()
race_time = int("".join(lines[0].split()[1:]))
record_distance = int("".join(lines[1].split()[1:]))
ways = 0

# Iterate over all possible hold times
for hold_time in tqdm(range(race_time), desc="Calculating"):
    total_distance = hold_time * (race_time - hold_time)
    if total_distance > record_distance:
        ways += 1

print(ways)
print("--- %s seconds ---" % (time.time() - starttime))
