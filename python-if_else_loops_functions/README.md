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
