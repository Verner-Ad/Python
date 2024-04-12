import sqlite3
from warnings import filterwarnings
filterwarnings("ignore")
import os
import cgitb
from http.server import HTTPServer, CGIHTTPRequestHandler

cgitb.enable()

if os.path.exists("painting.db"):
    os.remove("painting.db")
con = sqlite3.connect("painting.db")
cur = con.cursor()
script_file = open("script.sql", encoding="utf-8")
cur.executescript(script_file.read())
con.commit()



# cur.execute(query)
# for res in cur.fetchall():
#     print(res)
# print()



# cur.execute(query)
# for res in cur.fetchall():
#     print(res)
# print()

query = """SELECT * FROM PAINTING"""

cur.execute(query)
for res in cur.fetchall():
    print(res)

con.close()

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()