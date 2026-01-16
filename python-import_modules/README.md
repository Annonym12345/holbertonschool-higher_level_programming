# Git Intro Project

│ File: 0-add.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │
   3   │ if __name__ == "__main__":
   4   │     """Print the sum of 1 and 2."""
   5   │     from add_0 import add
   6   │
   7   │     a = 1
   8   │     b = 2
   9   │     print("{} + {} = {}".format(a, b, add(a, b)))
───────┴─────────────────────────────────────────────────────
┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 1-calculation.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │
   3   │ if __name__ == "__main__":
   4   │     """Print the sum, difference, multiple and quotient of 10 and 5."""
   5   │     from calculator_1 import add, sub, mul, div
   6   │
   7   │     a = 10
   8   │     b = 5
   9   │
  10   │     print("{} + {} = {}".format(a, b, add(a, b)))
  11   │     print("{} - {} = {}".format(a, b, sub(a, b)))
  12   │     print("{} * {} = {}".format(a, b, mul(a, b)))
  13   │     print("{} / {} = {}".format(a, b, div(a, b)))
───────┴───────────────────────────────────────────────────────────────────
