import sqlite3
conn = sqlite3.connect("Pidory.db")
cursor = conn.cursor()

cursor.execute("drop table Pidory")
cursor.execute("""
create table Pidory (

id integer,
username string
password string
);



""")

conn.commit()
conn.close()
conn = sqlite3.connect("Tasks.db")
cursor_1 = conn.cursor()

cursor_1.execute("drop table Tasks")
cursor_1.execute("""
create table Tasks (

id integer,
name string
type string
flag string
key string
text string
is_published bool
);



""")











conn.commit()
conn.close()
