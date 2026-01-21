# Git Intro Project

──┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-square_matrix_simple.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ def square_matrix_simple(matrix=[]):
   3   │     new_matrix = []
   4   │
   5   │     if len(matrix) > 0:
   6   │         for elems in matrix[:]:
   7   │             new_matrix.append(list(map(lambda x: x ** 2, elems)))
   8   │
   9   │     return new_matrix
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 10-best_score.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ def best_score(a_dictionary):
   3   │     if a_dictionary is None:
   4   │         return None
   5   │
   6   │     b_score = max(a_dictionary.values(), default=None)
   7   │     for k, v in a_dictionary.items():
   8   │         if v == b_score:
   9   │             return k
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 11-mutiply_list_map.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ def mutiply_list_map(my_list=[], number=0):
   3   │     return list(map(lambda x: x * number, my_list))
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 12-roman_to_int.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ def roman_to_int(roman_string):
   3   │     if type(roman_string) is not str or roman_string is None:
   4   │         return 0
   5   │
   6   │     roman_letters = [
   7   │         ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
   8   │         ['X', 10], ['V', 5], ['I', 1]
   9   │     ]
  10   │     num = 0
  11   │     last = 0
  12   │
  13   │     for letter in roman_string:
  14   │         for elem in roman_letters:
---------------------------------------------------------------------------------------------------
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(mul, my_list))

def mul(x):
    return x * number
