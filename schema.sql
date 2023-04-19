-- SQL for resetting schema:
-- $ sqlite3 test.sqlite3 < schema.sql
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS purchases;

CREATE TABLE contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL UNIQUE,
	last_name TEXT NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE,
	date_created TEXT NOT NULL
);
CREATE TABLE products (
	product_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	sku TEXT NOT NULL UNIQUE,
	price INTEGER NOT NULL
);
CREATE TABLE purchases (
	purchase_id INTEGER PRIMARY KEY,
	contact_id INTEGER REFERENCES contacts(contact_id),
	product_id INTEGER REFERENCES products(product_id),
	date_created TEXT NOT NULL
);
