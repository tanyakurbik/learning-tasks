# k = 2021
# n = 2
# a = "3000 1000"
k = int(input())
n = int(input())
a = input()
cards = a.split()
for i in range(len(cards)):
    cards[i] = int(cards[i])
sum_cards = sum(cards)
for j in cards:
    if (sum_cards - j) < k:
        flag = 'NO'
    else:
        flag = "YES"
print(flag)


