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
        if not input_arr[i][j].isdigit() and input_arr[i][j] != ".":
            symbols.append((i, j))
            if number != "":
                numbers[tuple(indices)] = number
                number = ""
                indices = [i]
        elif input_arr[i][j].isdigit():
            number += input_arr[i][j]
            indices.append((i, j))
        elif input_arr[i][j] == ".":
            if number != "":
                numbers[tuple(indices)] = number
                number = ""
                indices = [i]
    if number != "":
        numbers[tuple(indices)] = number


part_sum = 0
part_numbers = []
for key, value in numbers.items():
    neighbours = get_neighbours(key, ncols, nrows)
    if len([indice for indice in neighbours if indice in symbols]) > 0:
        part_sum += int(value)
        part_numbers.append(int(value))

print(part_sum)
print("--- %s seconds ---" % (time.time() - starttime))
