# Git Intro Project

──┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 00-main.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ # Main file content
   2   │ from task_00_intro import generate_invitations
   3   │
   4   │ # Read the template from a file
   5   │ with open('template.txt', 'r') as file:
   6   │     template_content = file.read()
   7   │
   8   │ # List of attendees
   9   │ attendees = [
  10   │     {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_
       │ location": "New York"},
  11   │     {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "even
       │ t_location": "San Francisco"},
  12   │     {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Bo
       │ ston"}
  13   │ ]
  14   │
  15   │ # Call the function with the template and attendees list
  16   │ generate_invitations(template_content, attendees)
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: create_db.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ import sqlite3
   2   │
   3   │ def create_database():
   4   │     conn = sqlite3.connect('products.db')
   5   │     cursor = conn.cursor()
   6   │
   7   │     cursor.execute('''
   8   │         CREATE TABLE IF NOT EXISTS Products (
   9   │             id INTEGER PRIMARY KEY,
  10   │             name TEXT NOT NULL,
  11   │             category TEXT NOT NULL,
  12   │             price REAL NOT NULL
  13   │         )
  14   │     ''')
  15   │
  16   │     cursor.execute('DELETE FROM Products')
  17   │
  18   │     cursor.execute('''
  19   │         INSERT INTO Products (id, name, category, price)
  20   │         VALUES
  21   │         (1, 'Laptop', 'Electronics', 799.99),
  22   │         (2, 'Coffee Mug', 'Home Goods', 15.99)
  23   │     ''')
  24   │
