import psycopg2
# Connect to the PostgreSQL database
conn = psycopg2.connect(
 host="postgres",
 database="mydatabase",
 user="myuser",
 password="mypassword"
)
# Run a SELECT query on the "mytable" table
cur = conn.cursor()
cur.execute("SELECT * FROM mytable")
rows = cur.fetchall()
for row in rows:
 print(row)
# Close the database connection
conn.close()
