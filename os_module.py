import os

# built in library
if not os.path.exists("data"):
    os.mkdir("data")  # directory made named data

for i in range(1, 3):
    os.mkdir(f"data/Day{i}")  # created 2 folders inside data with name Day1 and so on

os.rename(f"data/Day{i}",f"data/Day{i}")

