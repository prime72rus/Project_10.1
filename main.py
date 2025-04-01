import psycopg2


conn = psycopg2.connect(host="localhost", database="test", user="postgres", password="Neduryvyb032025")
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO post VALUES (%s, %s, %s, %s)", (6, 'Monday', '', 2))
            cur.execute("SELECT * FROM post")
            rows = cur.fetchall()
            for i in rows:
                print(i)
finally:
    conn.close()
