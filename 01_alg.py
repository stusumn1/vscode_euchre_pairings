import pandas as pd
from sklearn.datasets import load_iris
import random

letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

# Create sample emails
d = {'email': [1, 2], 'points': [4, 2]}
emails = pd.DataFrame(data = d)
print(emails)

email = ''
for _ in range(7):
    letter = random.sample(letters,1)[0]
    email += letter

email += '@gmail.com'
print(email)
