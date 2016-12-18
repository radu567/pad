import psycopg2


# conexiune la baza de date : nume baza de date, utilizator, parola, host, portul pe care se afla baza de date
conn = psycopg2.connect(database="db", user="postgres", password="1111", host="127.0.0.1", port="5432")
print("Conexiune realizata cu succes")

curs = conn.cursor()

curs.execute("SELECT id, informatie from info")
rows = curs.fetchall()

# print(rows)

for row in rows:
    print("id = ", row[0])
    print("informatie = ", row[1], "\n")

print("Realizat cu succes")
conn.close()
