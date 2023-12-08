import time

starttime = time.time()
lines = open("7/input.txt").readlines()

cards = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]  # A is high, 2 is low

example = lines


def rank_hand(hand):
    ranks = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    hand = sorted(hand, key=lambda card: ranks[card], reverse=True)
    counts = {rank: hand.count(rank) for rank in hand}
    if 5 in counts.values():
        return (7, ranks[hand[0]])
    elif 4 in counts.values():
        return (6, ranks[hand[0]], ranks[hand[4]])
    elif 3 in counts.values() and 2 in counts.values():
        return (5, ranks[hand[0]], ranks[hand[4]])
    elif 3 in counts.values():
        return (4, ranks[hand[0]], ranks[hand[3]], ranks[hand[4]])
    elif 2 in counts.values() and len(counts) == 3:
        pair1 = ranks[hand[1]] if hand[0] == hand[1] else ranks[hand[3]]
        pair2 = ranks[hand[1]] if hand[0] != hand[1] else ranks[hand[3]]
        return (3, max(pair1, pair2), min(pair1, pair2), ranks[hand[4]])
    elif 2 in counts.values():
        return (2, ranks[hand[1]], ranks[hand[0]], ranks[hand[3]], ranks[hand[4]])
    else:
        return (
            1,
            ranks[hand[0]],
            ranks[hand[1]],
            ranks[hand[2]],
            ranks[hand[3]],
            ranks[hand[4]],
        )


def sort_hands(hands):
    return sorted(hands, key=rank_hand, reverse=True)


# Remove the bets from the lines for now, but re-add them later
bets = []
for i in range(len(example)):
    line = example[i].strip()
    bet = line.split(" ")[-1]
    bets.append(bet)
    example[i] = line[: -len(bet)].strip()
    # example[i] = "".join(example[i])

hands = []
for line in example:
    hand = line.split(" ")
    hand = "".join(hand)
    hands.append(hand)

for i in range(len(hands)):
    print("The bet for {} is {}".format(hands[i], bets[i]))

# Sort
sorted_hands = sort_hands(hands)

# Create a dictionary to map hands to bets
hand_to_bet = {hand: bet for hand, bet in zip(hands, bets)}

# Determine total winnings by multiplying bet * rank and add to total
total = 0

for i in range(len(sorted_hands)):
    print(i)
    total += int(hand_to_bet[sorted_hands[i]]) * (i + 1)

print(total)
print("--- %s seconds ---" % (time.time() - starttime))
