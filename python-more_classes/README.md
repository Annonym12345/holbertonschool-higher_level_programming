# Git Intro Project

┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-rectangle.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """
   3   │
   4   │ A module with a Rectangle that does nothing
   5   │
   6   │ """
   7   │
   8   │
   9   │ class Rectangle:
  10   │     """
  11   │
  12   │     An empty Rectangle class
  13   │
  14   │     """
  15   │
  16   │     pass
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
─┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 1-rectangle.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """
   3   │
   4   │ A module with a Rectangle that does nothing
   5   │
   6   │ """
   7   │
   8   │
   9   │ class Rectangle:
  10   │     """
  11   │
  12   │     An empty Rectangle class
  13   │
  14   │     """
  15   │
  16   │     def __init__(self, width=0, height=0):
  17   │         """
  18   │
  19   │         Checks the parameters and initializes some values
  20   │
  21   │         Args:
  22   │             width (:obj:`int`, optional): The width of the Rectangle.
  23   │             height (:obj:`int`, optional): The height of the Rectangle.
  24   │
  25   │         """
  26   │
  27   │         self.__check_valid_width(width)
  28   │         self.__check_valid_height(height)
  29   │
  30   │         self.width = width
  31   │         self.height = height
  32   │
  33   │     @property
  34   │     def width(self):
  35   │         """
  36   │
  37   │         Returns the width of the Rectangle
  38   │
  39   │         """
  40   │
  41   │         return self.__width
  42   │
  43   │     @width.setter
  44   │     def width(self, value):
  45   │         """
  46   │
  47   │         Checks the parameters and set the size of the Rectangle
