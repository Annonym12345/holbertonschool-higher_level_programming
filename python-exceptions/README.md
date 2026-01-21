# Git Intro Project

───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-safe_print_list.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │
   3   │
   4   │ def safe_print_list(my_list=[], x=0):
   5   │     idx = 0
   6   │
   7   │     try:
   8   │         for i in my_list:
   9   │             if idx < x:
  10   │                 print('{}'.format(my_list[idx]), end='')
  11   │                 idx += 1
  12   │
  13   │         print()
  14   │     except TypeError:
  15   │         pass
  16   │     finally:
  17   │         return idx
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 1-safe_print_integer.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │
   3   │
   4   │ def safe_print_integer(value):
   5   │     try:
   6   │         print('{:d}'.format(value))
   7   │         return True
   8   │     except (TypeError, ValueError):
   9   │         return False
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 2-safe_print_list_integers.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │
   3   │
   4   │ def safe_print_list_integers(my_list=[], x=0):
   5   │     printed = 0
   6   │
   7   │     for i in range(x):
   8   │         try:
   9   │             if type(my_list[i]) is int and printed != x:
  10   │                 print('{:d}'.format(my_list[i]), end='')
  11   │                 printed += 1
  12   │         except TypeError:
  13   │             continue
