from warnings import filterwarnings
import cgi
import sqlite3

# ignore msg that cgi is deprecated
filterwarnings("ignore")

form = cgi.FieldStorage()
FIRST_NAME = form.getfirst("FIRST_NAME")
SURNAME = form.getfirst("SURNAME")
SEX = form.getfirst("SEX")

PIC_NAME = form.getfirst("PIC_NAME")
CRE_DATE = form.getfirst("CRE_DATE")
GENRE = form.getfirst("GENRE")
MATERIAL = form.getfirst("MATERIAL")
HEIGHT = form.getfirst("HEIGHT")
WIDTH = form.getfirst("WIDTH")
AUTHOR_ID = form.getfirst("AUTHOR_ID")
GALLERY_ID = form.getfirst("GALLERY_ID")

if HEIGHT:
    HEIGHT = int(HEIGHT)
if WIDTH:
    WIDTH = int(WIDTH)
if AUTHOR_ID:
    AUTHOR_ID = int(AUTHOR_ID)
if GALLERY_ID:
    GALLERY_ID = int(GALLERY_ID)

con = sqlite3.connect("painting.db")
cur = con.cursor()

if all((FIRST_NAME, SURNAME, SEX)):
    query = f"INSERT INTO address (FIRST_NAME, SURNAME, SEX) VALUES ('{FIRST_NAME}', '{SURNAME}', '{SEX}')"
    cur.execute(query)
    con.commit()

if all((PIC_NAME, CRE_DATE, GENRE, MATERIAL, HEIGHT, WIDTH, AUTHOR_ID, GALLERY_ID)):
    query = f"INSERT INTO person (PIC_NAME, CRE_DATE, GENRE, MATERIAL, HEIGHT, WIDTH, AUTHOR_ID, GALLERY_ID) VALUES ('{PIC_NAME}', '{CRE_DATE}', '{GENRE}', '{MATERIAL}', '{HEIGHT}', '{WIDTH}', '{AUTHOR_ID}', '{GALLERY_ID}')"
    cur.execute(query)
    con.commit()
    
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')