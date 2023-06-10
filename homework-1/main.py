"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

with psycopg2.connect(host="localhost", database="north", user="postgres", password="123456") as conn:
    with conn.cursor() as cur:
        with open("north_data/customers_data.csv", "r", encoding="utf-8") as file:
            list_file = file.readlines()
            for line in list_file[1:]:
                row_list = line.split('","')
                cur.execute("INSERT INTO customers_data VALUES (%s, %s, %s)",
                            (row_list[0].strip('"'), row_list[1].strip('"'), row_list[2].strip("\n").strip('"')))
                cur.execute("SELECT * FROM customers_data")

    with conn.cursor() as cur:
        with open("north_data/employees_data.csv", "r", encoding="utf-8") as file:
            list_file = file.readlines()
            for line in list_file[1:]:
                row_list = line.split(',"')
                cur.execute("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)",
                            (row_list[0].strip('"'), row_list[1].strip('"'), row_list[2].strip('"'), row_list[3].strip('"'), row_list[4].strip('"'), row_list[5].strip("\n").strip('"')))
                cur.execute("SELECT * FROM employees_data")

    with conn.cursor() as cur:
        with open("north_data/orders_data.csv", "r", encoding="utf-8") as file:
            list_file = file.readlines()
            for line in list_file[1:]:
                row_list = line.split(',')
                cur.execute("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)",
                            (row_list[0].strip('"'), row_list[1].strip('"'), row_list[2].strip('"'), row_list[3].strip('"'), row_list[4].strip("\n").strip('"')))
                cur.execute("SELECT * FROM orders_data")

conn.close()
