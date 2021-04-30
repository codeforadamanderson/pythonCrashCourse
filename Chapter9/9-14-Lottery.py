from random import choice

lottery_list = [1, 3, 5, 7, 9, 'a', 'b', 'c', 'd', 'e']
lottery_winners = []

while len(lottery_winners) < 5:
    winning_entry = choice(lottery_list)
    if winning_entry not in lottery_winners:
        lottery_winners.append(winning_entry)

print("\nThe winning entries are:")
for entry in lottery_winners:
    print(entry)