# Git Intro Project

───┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-select_states.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """
   3   │ 0-select_states.py
   4   │
   5   │ Lists all states from the database hbtn_0e_0_usa
   6   │ """
   7   │ import MySQLdb
   8   │ import sys
   9   │
  10   │
  11   │ if __name__ == "__main__":
  12   │     """
  13   │     Main function:
  14   │     that executes the database
  15   │     connection and retrieval of states.
  16   │     """
  17   │
  18   │     username = sys.argv[1]
  19   │     password = sys.argv[2]
  20   │     database = sys.argv[3]
  21   │
  22   │     db = MySQLdb.connect(
  23   │         host="localhost",
  24   │         user=username,
  25   │         passwd=password,
  26   │         db=database,
  27   │         port=3306
  28   │     )
  29   │     cursor = db.cursor()
  30   │     cursor.execute("SELECT * FROM states ORDER BY id ASC")
  31   │     states = cursor.fetchall()
  32   │
  33   │     for state in states:
  34   │         print(state)
  35   │
  36   │     cursor.close()
  37   │     db.close()
───────┴──────────────────────────────────────────────────────────
