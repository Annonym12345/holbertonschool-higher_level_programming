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
──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 2-args.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │
   3   │ if __name__ == "__main__":
   4   │     """Print the number of and list of arguments."""
   5   │     import sys
   6   │
   7   │     count = len(sys.argv) - 1
   8   │     if count == 0:
   9   │         print("0 arguments.")
  10   │     elif count == 1:
  11   │         print("1 argument:")
  12   │     else:
  13   │         print("{} arguments:".format(count))
  14   │     for i in range(count):
  15   │         print("{}: {}".format(i + 1, sys.argv[i + 1]))
───────┴─────────────────────────────────────────────────────────────────────────────────────────────
