import pytz
from datetime import datetime
import pandas as pd

london_dt = pytz.timezone('Europe/London')
newyork_dt = pytz.timezone('America/New_York')
portland_dt = pytz.timezone('America/Los_Angeles')

x = datetime.now(london_dt).hour
y = datetime.now(newyork_dt).hour
z = datetime.now(portland_dt).hour

print(x)

if x == 9:
    print("The London office is open.")
elif x == 10:
    print("The London office is open.")
elif x == 11:
    print("The London office is open.")
elif x == 12:
    print("The London office is open.")
elif x == 13:
    print("The London office is open.")
elif x == 14:
    print("The London office is open.")
elif x == 15:
    print("The London office is open.")
elif x == 16:
    print("The London office is open.")
else:
    print("The London office is closed")

print(y)

if y == 9:
    print("The New York office is open.")
elif y == 10:
    print("The New York office is open.")
elif y == 11:
    print("The New York office is open.")
elif y == 12:
    print("The New York office is open.")
elif y == 13:
    print("The New York office is open.")
elif y == 14:
    print("The New York office is open.")
elif y == 15:
    print("The New York office is open.")
elif y == 16:
    print("The New York office is open.")
else:
    print("The New York office is closed")

print(z)

if z == 9:
    print("The Portland office is open.")
elif z == 10:
    print("The Portland office is open.")
elif z == 11:
    print("The Portland office is open.")
elif z == 12:
    print("The Portland office is open.")
elif z == 13:
    print("The Portland office is open.")
elif z == 14:
    print("The Portland office is open.")
elif z == 15:
    print("The Portland office is open.")
elif z == 16:
    print("The Portland office is open.")
else:
    print("The Portland office is closed")
