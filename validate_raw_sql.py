"""Parse queries.csv, extracting baseline queries validating them."""
import csv
import sqlite3
import sys

from yachalk import chalk


con = sqlite3.connect("northwind.db")
cur = con.cursor()
try:
    with open('./queries.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=":")
        for row in list(reader)[1:]:
            free_text = row[0]
            sql = row[1]
            print(free_text)
            print(chalk.gray(f'Querying: {sql}'))
            res = cur.execute(sql).fetchall()
            for row in res:
                print(chalk.gray("".join([str(col) for col in row])))
            print(chalk.green("success!"))
            print()
except Exception as err:
    print(chalk.red(f'Problem running query: {err}'))
    sys.exit(1)
finally:
    con.close()