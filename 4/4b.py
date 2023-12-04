from tqdm import tqdm
import time

starttime = time.time()


def parse_card(card):
    winning_numbers = card.split(": ")[1].split(" | ")[0]
    my_numbers = card.split(": ")[1].split(" | ")[1]
    return set(map(int, winning_numbers.split())), set(map(int, my_numbers.split()))


def count_matches(card):
    winning_numbers, my_numbers = card
    return len(winning_numbers & my_numbers)


def process_cards(cards):
    total_cards = len(cards)
    card_copies = [1] * total_cards
    for i in tqdm(range(total_cards)):
        matches = count_matches(cards[i])
        for j in range(i + 1, min(i + 1 + matches, total_cards)):
            card_copies[j] += card_copies[i]
    return sum(card_copies)


input_data = open("4/input.txt", "r").read()
cards = [parse_card(card) for card in input_data.split("\n")]
print(process_cards(cards))
print("--- %s seconds ---" % (time.time() - starttime))
