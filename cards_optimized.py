def solve(k, _, a):
    k = int(k)
    cards = tuple(int(x) for x in a.split())
    sum_cards = sum(cards)
    for j in cards:
        if sum_cards - j > k:
            return "YES"
    return "NO"


assert solve("2000", "4", "20 200 400 900") == "NO"
assert solve("1800", "4", "20 200 400 900") == "NO"
assert solve("1700", "4", "20 200 400 900") == "NO"
assert solve("1300", "4", "20 200 400 900") == "YES"
assert solve("1200", "4", "20 200 400 900") == "YES"
print(solve(input(), input(), input()))
