# Git Intro Project

─┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-positive_or_negative.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1 ~ │ #!/usr/bin/python3
   2 _ │ import random
   3 _ │ number = random.randint(-10, 10)
   4   │ if number > 0:
   5   │     print("{} is positive".format(number))
   6   │ elif number == 0:
   7   │     print("{} is zero".format(number))
   8   │ else:
   9   │     print("{} is negative".format(number))
───────┴────────────────────────────────────────────────────────────────────────
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")

 │ File: 2-print_alphabet.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ # 2-print_alphabet.py
   3   │ # Annonym12345 <ismaelbsd.pro@gmail.com>
   4   │
   5   │ """Print the alphabet in lowercase, not followed by a new line."""
   6   │ for letter in range(97, 123):
   7   │     print("{}".format(chr(letter)), end="")
───────┴───────────────────────────────────────────────────────────
#!/usr/bin/python3
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
print("guillaume", end="")

