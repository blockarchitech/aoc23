import time

start_time = time.time()
lines = open("2/input.txt", "r").readlines()


get_id = lambda l: int(l.split(":")[0].split(" ")[1])


def check_possible(l):
    id = get_id(l)
    l = l.split(": ")[1]
    l = l[:-1]
    rounds = l.split("; ")
    values = []
    highest = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for round in rounds:
        round_value = []
        moves = round.split(", ")
        for move in moves:
            values = move.split(" ")
            round_value.append(int(values[0]))
            if int(values[0]) > highest[values[1]]:
                highest[values[1]] = int(values[0])
    power = lambda h: h["red"] * h["green"] * h["blue"]
    return {"id": id, "power": power(highest), "highest": highest}


powers = []
for line in lines:
    powers.append(check_possible(line)["power"])

print(sum(powers))
print("--- %s seconds ---" % (time.time() - start_time))
