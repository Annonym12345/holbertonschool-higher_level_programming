#!/usr/bin/python3
txt = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(txt[39:67] + txt[107:112] + txt[:6].strip('P'))
