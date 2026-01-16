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
--------------------------------------------------------------------------------
#!/usr/bin/python3

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
---------------------------------------------------------------------------
#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
----------------------------------------------------------------------------
#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
----------------------------------------------------------------------------------
#!/usr/bin/python3

def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
