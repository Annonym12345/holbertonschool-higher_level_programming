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

────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 10-model_state_my_get.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """Task: List all states that contain the letter 'a'"""
   3   │ import sys
   4   │ from model_state import State, Base
   5   │ from sqlalchemy import create_engine
   6   │ from sqlalchemy.orm import sessionmaker
   7   │
   8   │
   9   │ if __name__ == "__main__":
  10   │     connect = create_engine(
  11   │         "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
  12   │             sys.argv[1],
  13   │             sys.argv[2],
  14   │             sys.argv[3]),
  15   │         pool_pre_ping=True)
  16   │     Session = sessionmaker(bind=connect)
  17   │     session = Session()
  18   │     States = session.query(State).filter(State.name == sys.argv[4]).first()
  19   │
  20   │     if States is not None:
  21   │         print(States.id)
  22   │     else:
  23   │         print("Not found")
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 11-model_state_insert.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """Task: Add the Louisiana state to the database"""
   3   │ import sys
   4   │ from model_state import State, Base
   5   │ from sqlalchemy import create_engine
   6   │ from sqlalchemy.orm import sessionmaker
   7   │
   8   │
   9   │ if __name__ == "__main__":
  10   │     connect = create_engine(
  11   │         "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
  12   │             sys.argv[1],
  13   │             sys.argv[2],
  14   │             sys.argv[3]),
  15   │         pool_pre_ping=True)
  16   │     Base.metadata.create_all(connect)
  17   │     Session = sessionmaker(bind=connect)
  18   │     session = Session()
  19   │     new_state = State(name='Louisiana')
  20   │     session.add(new_state)
