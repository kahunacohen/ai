'''This script produces the jsonl from the csv file. After this is run,
$ openai tools fine_tunes.prepare_data -f queries.jsonl'''
from yachalk import chalk
import pandas as pd


data = pd.read_csv("./queries.csv", delimiter=":").drop(columns=['training'])
print("\nFirst 10 lines of data parsed from queries.csv:")
print(chalk.gray(data.head()))
data.to_json("queries.jsonl",orient='records',lines=True)
print(chalk.green("Succesfully translated .csv files to queries.jsonl file."))
