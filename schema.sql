CREATE TABLE contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE products (
	product_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	sku TEXT NOT NULL,
	price INTEGER
);
CREATE TABLE purchases (
	purchase_id INTEGER PRIMARY KEY,
	contact_id INTEGER REFERENCES contacts(contact_id),
	product_id INTEGER REFERENCES products(product_id)
);
