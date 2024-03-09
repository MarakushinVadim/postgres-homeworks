"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# задаем параметры для БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Oblivion94$'
)

# оборачивам в блок try/finally для сокращения кода
try:
    with conn:
        # считываем через стандартный readlines
        with open('north_data/customers_data.csv', encoding='UTF-8') as file:
            raws = file.readlines()
            for raw in range(1, len(raws)):
                splited_raw = raws[raw].split(',')
                # записываем в нелбходимую таблицу
                with conn.cursor() as cur:
                    cur.execute(
                        'INSERT INTO customers VALUES (%s, %s, %s)',
                        (splited_raw[0],
                         splited_raw[1],
                         splited_raw[2]
                         )
                    )
        # считываем через csv reader
        with open('north_data/employees_data.csv', 'r', newline='', encoding='UTF-8') as file:
            raws = csv.reader(file)
            next(raws)
            for raw in raws:
                # записываем в нелбходимую таблицу
                with conn.cursor() as cur:
                    cur.execute(
                        'INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                        (int(raw[0]),
                         raw[1],
                         raw[2],
                         raw[3],
                         raw[4],
                         raw[5])
                    )

        with open('north_data/orders_data.csv', 'r', newline='', encoding='UTF-8') as file:
            # считываем через csv reader
            raws = csv.reader(file)
            next(raws)
            for raw in raws:
                # записываем в нелбходимую таблицу
                with conn.cursor() as cur:
                    cur.execute(
                        'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                        (raw[0],
                        raw[1],
                        raw[2],
                        raw[3],
                        raw[4])
                    )
# делаем коммит
finally:
    conn.close()
