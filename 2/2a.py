import time

start_time = time.time()
lines = open("2/input.txt", "r").readlines()


limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


get_id = lambda l: int(l.split(":")[0].split(" ")[1])


def check_possible(l):
    id = get_id(l)
    l = l.split(": ")[1]
    l = l[:-1]
    rounds = l.split("; ")
    for round in rounds:
        moves = round.split(", ")
        for move in moves:
            values = move.split(" ")
            if int(values[0]) > limits[values[1]]:
                print(
                    "Game "
                    + str(id)
                    + " is not possible! ("
                    + str(values[0])
                    + " > "
                    + str(limits[values[1]])
                    + " "
                    + values[1]
                    + ")"
                )
                return False
    print("Game " + str(id) + " is possible!")
    return True


values = []

for line in lines:
    if check_possible(line):
        values.append(get_id(line))


print(sum(values))
print("--- %s seconds ---" % (time.time() - start_time))
