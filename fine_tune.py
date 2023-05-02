import pandas as pd
print("hi")

data = pd.read_csv("./queries.csv", header=None, delimiter=":")
print(data)
