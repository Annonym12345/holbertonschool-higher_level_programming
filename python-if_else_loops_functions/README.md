# Git Intro Project

──┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-positive_or_negative.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1 _ │ #!/usr/bin/env python3
   2   │ import random
   3   │
   4   │ number = random.randint(-10, 10)
   5   │
   6   │ if number > 0:
   7 ~ │     print("{} is positive".format(number))
   8   │ elif number == 0:
   9 ~ │     print("{} is zero".format(number))
  10   │ else:
  11 ~ │     print("{} is negative".format(number))
───────┴──────────────────────────────────────────────────────
