import psycopg2
import os
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

cur.execute("select nome, endereco, id from usuarios where data_cadastro >= '2026-01-01'")
res = cur.fetchall()

arquivo = open('./stg/users.csv', 'w')

for linhas in res:
    arquivo.write(','.join(map(str, linhas)) + '\n')

arquivo.close()

