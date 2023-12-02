import re
import time

start_time = time.time()

lines = open("1/input.txt", "r").readlines()

spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

example = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def find(l):
    first = re.compile(
        r"(" + "|".join("{k}|{v}".format(k=k, v=v) for k, v in spelled.items()) + r")"
    )
    last = re.compile(
        r"(" + "|".join("{k}|{v}".format(k=k, v=v) for k, v in spelled.items()) + r")"
    )

    return [first.findall(l)[0], last.findall(l)[-1]]


values = []

for line in lines:
    parsed = find(line)
    first = ""
    last = ""
    try:
        first = int(parsed[0])
    except ValueError:
        first = spelled[parsed[0]]
    try:
        last = int(parsed[1])
    except ValueError:
        last = spelled[parsed[1]]
    first = str(first)
    last = str(last)
    values.append(int(first + last))

print(sum(values))
print("--- %s seconds ---" % (time.time() - start_time))
