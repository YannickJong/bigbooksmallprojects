import sys

print(f"""
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
    If n is even, the next number n is n/2.
    If n is uneven, the next number n is 3n+1
    If n is 1, stop. Otherwise, repeat.

Enter a starting number (greater than 0) or QUIT:""")

while True:
    n = input("> ")
    if n.lower().startswith("q"):
        sys.exit()
    elif n.isnumeric() and int(n) > 0:
        n = int(n)
        break

seq = [n]
while seq[-1] != 1:
    if seq[-1] % 2 == 0:
        seq.append(int(seq[-1]/2))
    else:
        seq.append(int(seq[-1]*3+1))

seq = [str(i) for i in seq]
print(", ".join(seq))
