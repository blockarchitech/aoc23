import time

starttime = time.time()
lines = open("4/input.txt", "r").readlines()
example = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def calculate_points(line):
    card_name, numbers = line.split(": ")
    set1, set2 = numbers.split(" | ")
    set1 = list(map(int, set1.split()))
    set2 = list(map(int, set2.split()))
    winning_numbers = set(set1) & set(set2)
    print(f"Winning numbers for {card_name}: {winning_numbers}")  # Debugging line
    matches = len(winning_numbers)
    points = 1 if matches > 0 else 0
    for _ in range(1, matches):
        points *= 2
    return card_name, points


total_points = 0
for line in lines:
    _, points = calculate_points(line)
    total_points += points

print(f"Total points: {total_points}")  # Debugging line
print("--- %s seconds ---" % (time.time() - starttime))
