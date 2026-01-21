# Git Intro Project
  │ File: 0-add_integer.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """A module to add two numbers
   3   │
   4   │ This module performs the addition operation between two numbers,
   5   │ these numbers can be integers or floats.
   6   │
   7   │ """
   8   │
   9   │
  10   │ def add_integer(a, b=98):
  11   │     """Adds two numbers
  12   │
  13   │     Performs the addition between two numbers.
  14   │
  15   │     Args:
  16   │         a (:obj:`int, float`): The first number.
  17   │         b (:obj:`int, float`, optional): The second number.
  18   │
  19   │     Returns:
  20   │         int: The result of the addition.
  21   │
  22   │     """
  23   │     if type(a) not in (int, float):
  24   │         raise TypeError('a must be an integer')
  25   │
  26   │     if type(b) not in (int, float):
  27   │         raise TypeError('b must be an integer')
  28   │
  29   │     a = convert_to_int(a)
  30   │     b = convert_to_int(b)
  31   │     return a + b
  32   │
  33   │
  34   │ def convert_to_int(num):
  35   │     """Cast the data type of num parameter
  36   │
  37   │     Convert a float number to a integer number
  38   │
  39   │     Args:
  40   │         num (:obj:`int, float`): The number to cast.
  41   │
  42   │     Returns:
  43   │         int: The number casted to integer.
  44   │
  45   │     """
  46   │     if type(num) is float:
  47   │         num = int(num)
  48   │         return num
