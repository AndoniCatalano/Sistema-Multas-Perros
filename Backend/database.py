import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

conexion = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    dbname = os.getenv("DB_NAME"),
    port = os.getenv("DB_PORT")
)

cursor = conexion.cursor(cursor_factory=RealDictCursor)
