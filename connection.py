import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv('USER')
PASS = os.getenv('PASS')
PORT = os.getenv('PORT')
DB = os.getenv('DB')

conn = psycopg2.connect(
    database=DB, user=USER, password=PASS, host="localhost", port=PORT
)

cursor = conn.cursor()

cursor.execute("select version()")

data = cursor.fetchone()
print("Connection established to:", data)

conn.close()
