deck = input().split(" ")
shuffles = int(input())
shuffled = []

# VAR 1 #
# for _ in range(shuffles):
#     shuffled = []
#     for i in range(int(len(deck)/2)):
#         for card in deck[i::int(len(deck)/2)]:
#             shuffled.append(card)
#     deck = shuffled

# VAR 2 #
#
for _ in range(shuffles):
    deck_1 = deck[:int(len(deck) / 2)]
    deck_2 = deck[int(len(deck) / 2):]
    for index, card in enumerate(range(1, len(deck), 2)):
        deck_1.insert(card, deck_2[index])
        deck = deck_1

shuffled = deck

print(shuffled)
