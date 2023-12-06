import time

starttime = time.time()
lines = open("6/input.txt").readlines()
times = lines[0].split()[1:]
distances = lines[1].split()[1:]
races = [{"time": times[i], "distance": distances[i]} for i in range(len(times))]

multiply_arr = lambda arr: arr[0] * multiply_arr(arr[1:]) if len(arr) > 1 else arr[0]
get_distance = lambda time, speed: time * speed
get_time = lambda distance, speed: distance / speed
get_speed = lambda distance, time: distance / time

final_ways = []
for i in races:
    ways = 0
    racetime = int(i["time"])
    distance = int(i["distance"])
    for hold_time in range(racetime):
        speed = hold_time
        remaining_time = racetime - hold_time
        if remaining_time * speed > distance:
            ways += 1
    final_ways.append(ways)

print(multiply_arr(final_ways))
print("--- %s seconds ---" % (time.time() - starttime))
