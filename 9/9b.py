import time

starttime = time.time()


def previous_value(numbers):
    if len(numbers) == 1:
        return numbers[0]
    differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    return numbers[0] - previous_value(differences)


def sum_of_previous_values(histories):
    return sum(previous_value(history) for history in histories)


def read_histories(filename):
    with open(filename, "r") as file:
        histories = [[int(num) for num in line.split()] for line in file]
    return histories


def main():
    histories = read_histories("9/input.txt")
    print(sum_of_previous_values(histories))


main()
print("--- %s seconds ---" % (time.time() - starttime))
