import time

starttime = time.time()

with open("3/input.txt") as file:
    lines = [list(line) for line in file.read().strip().split("\n")]


def get_neighbours(tuple, ncols, nrows):
    cols = sorted([tuple[i][1] for i in range(1, len(tuple))])
    neighbours = []
    for i in range(tuple[0] - 1, tuple[0] + 2):
        for j in range(cols[0] - 1, cols[-1] + 2):
            if 0 <= i < nrows and 0 <= j < ncols and (i, j) not in tuple:
                neighbours.append((i, j))
    return neighbours


nrows = len(lines)
ncols = len(lines[0])

symbols = []
numbers = {}
for i in range(nrows):
    number = ""
    indices = [i]
    for j in range(ncols):
        if not lines[i][j].isdigit() and lines[i][j] != ".":
            symbols.append((i, j))
            if number != "":
                numbers[tuple(indices)] = number
                number = ""
                indices = [i]
        elif lines[i][j].isdigit():
            number += lines[i][j]
            indices.append((i, j))
        elif lines[i][j] == ".":
            if number != "":
                numbers[tuple(indices)] = number
                number = ""
                indices = [i]
    if number != "":
        numbers[tuple(indices)] = number


gear_sum = 0
visited = []
for i in range(nrows):
    for j in range(ncols):
        if lines[i][j] == "*":
            neighbours = get_neighbours([i, (i, j)], ncols, nrows)
            neighbour_numbers = []
            for neighbour in neighbours:
                if neighbour not in visited and len(neighbour_numbers) < 2:
                    for key, value in numbers.items():
                        if neighbour in key:
                            neighbour_numbers.append(int(value))
                            visited += list(key[1:])
            if len(neighbour_numbers) == 2:
                gear_sum += neighbour_numbers[0] * neighbour_numbers[1]

print(gear_sum)
print("--- %s seconds ---" % (time.time() - starttime))
