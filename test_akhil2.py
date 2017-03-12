import os

for root, dirs, files in os.walk("pickles/stock"):
    for file in files:
        print(str(file))
