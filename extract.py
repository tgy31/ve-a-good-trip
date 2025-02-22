import psycopg2
import psycopg2.extras


conn=psycopg2.connect(
  database="tanguydb",
  user="postgres",
  host = "localhost",
  port = 5432,
  password ="motdepasse",
  cursor_factory = psycopg2.extras.NamedTupleCursor,
  )
  

 