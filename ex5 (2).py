import sqlite3
connection = sqlite3.connect('book.sql')
cursor = connection.cursor()

sqlcommand = """
CREATE TABLE books(
book_id int,
title_id int,
location varchar(20),
genre varchar(20)
PRIMARY KEY(book_id)
FOREIGN KEY(title_id) REFERENCES titles(title_id));"""

cursor.execute(sqlcommand)

sqlcommand = """
CREATE TABLE titles(
title_id int,
title varchar(20),
ISBN int,
publisher_id int,
publiction_year
PRIMARY KEY(title_id);"""

cursor.execute(sqlcommand)

sqlcommand = """
CREATE TABLE publishers(
publisher_id int,
name varcahar(20),
street_address varchar(20),
suite_number int,
zip_code_id int );"""

cursor.execute(sqlcommand)

sqlcommand = """
CREATE TABLE zip_codes(
zip_code_id int,
