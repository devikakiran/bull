import random
digits = list("123456789")
random.shuffle(digits)
secret = "".join(digits[:4])
while True:
    g = input("Guess 4 unique digits (1-9): ")
    if len(g) != 4 or not g.isdigit() or "0" in g or len(set(g)) != 4:
        print("Bad guess.")
        continue
    if g == secret:
        print("You got it!", secret)
        break
    bulls = 0
    cows = 0
    for i in range(4):
        if g[i] == secret[i]:
            bulls += 1
        elif g[i] in secret:
            cows += 1
            print(bulls, "Bulls,", cows, "Cows")
