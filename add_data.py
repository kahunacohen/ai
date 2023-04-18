"""A script for generating a test db for sqlite3 for experimenting
with AI generation of SQL via fine-tuning. See schema.sql for generating
tables from scratch. This script populates tables with data, generating:

- A many-to-many relation between contacts and products via a through-table
  called purchases.
"""

import random
import sqlite3

import names

def generate_phone():
    sequence = []
    for i in range(7):
        sequence.append(str(random.randint(0, 9)))
    return "".join(sequence)

contacts = [(names.get_first_name(), names.get_last_name(), f"{i}@gmail.com", generate_phone()) for i in range(20)]
		
products = [
	("Shower Head", "abc", 1500),
	("Flusher handle", "abd", 1000),
	("Crazy Glue", "abe", 500),
	("Deluxe Paint Brush", "abf", 1000),
	("5' Ladder", "abg", 5000),
	("Cement", "abh", 1500),
	("Caulk", "abi", 500),
	("Pipe Fitting", "abj", 300 ),
	("Industrial Portable Heater", "abk", 50000),
	("Window", "abl", 25099),
	("Blinds", "abm", 37589),
	("Door", "abn", 45000),
	("Curtain Rod", "abo", 1545),
	("Drill", "abp", 25000),
	("Hammer", "abq", 1234),
	("Sink", "abr", 37500),
	("Mirror", "abs", 4089),
	("Work Bench", "abt", 56798),
	("Outdoor Furniture Set", "abu", 39900),
	("Stainless Steel Appliance Package", "abv", 264800),
]
def getcon():
	return sqlite3.connect("test.sqlite3")


def add_contacts():
	con = getcon()
	cur = con.cursor()
	try:
		cur.execute("DELETE FROM contacts")
		for c in contacts:
			q = f'''INSERT INTO contacts (first_name,last_name,email,phone)
	    				   VALUES("{c[0]}","{c[1]}","{c[2]}","{c[3]}");'''
			print(q)
			cur.execute(q)
		con.commit()
	except Exception as er:
		print(f'Error: {er}')
	finally:
		con.close()

def add_products():
	con = getcon()
	cur = con.cursor()
	try:
		cur.execute("DELETE FROM products;")
		for p in products:
			q = f'''INSERT INTO products (name,sku,price)
				VALUES("{p[0]}", "{p[1]}", "{p[2]}");'''
			print(q)
			cur.execute(q)
		con.commit()
	except Exception as er:
		print(f'Error: {er}')
	finally:
		con.close()

def make_purchases():
	con = getcon()
	cur = con.cursor()
	try:
		cur.execute("DELETE from purchases;")
		for i,c in enumerate(contacts[:len(products)]):
			c_id = i + 1	
			product = products[i]
			q = f'''INSERT INTO purchases (contact_id,product_id)
				VALUES("{c_id}", "{random.randint(1, 20)}")'''
			print(q)
			con.execute(q)
			con.commit()
	except Exception as er:
		print(f'Error: {err}')
	finally:
		con.close()
		

add_contacts()
add_products()
make_purchases()
