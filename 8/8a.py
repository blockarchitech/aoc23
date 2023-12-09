import time

starttime = time.time()
lines = open("8/input.txt").readlines()

instructions = lines[0].strip()

nodes = {}
for line in lines[1:]:
    if line.strip() == "":
        continue
    line = line.strip()
    print(line)
    print(line.split(" = "))
    node, children = line.split(" = ")
    children = children[1:-1].split(", ")
    nodes[node] = children

current_node = "AAA"
path = [current_node]
steps = 0

while current_node != "ZZZ":
    instruction = instructions[steps % len(instructions)]
    children = nodes[current_node]

    if instruction == "R":
        current_node = children[1]
    elif instruction == "L":
        current_node = children[0]

    path.append(current_node)
    steps += 1

print(path, "-", steps)
print("--- %s seconds ---" % (time.time() - starttime))
