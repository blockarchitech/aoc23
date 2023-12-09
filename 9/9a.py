import time

starttime = time.time()
lines = open("9/input.txt").readlines()


def next_value(numbers):
    if len(numbers) == 1:
        return numbers[0]
    differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    return next_value(differences) + numbers[-1]


def sum_of_next_values(histories):
    return sum(next_value(history) for history in histories)


def read_histories(filename):
    with open(filename, "r") as file:
        histories = [[int(num) for num in line.split()] for line in file]
    return histories


def main():
    histories = read_histories("9/input.txt")
    print(sum_of_next_values(histories))


main()
print("--- %s seconds ---" % (time.time() - starttime))
