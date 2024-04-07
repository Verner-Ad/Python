from warnings import filterwarnings
import cgi
import sqlite3

# ignore msg that cgi is deprecated
filterwarnings("ignore")

def prepare_row(row):
    row = list(map(lambda value: f"<td>{value}</td>", row))
    row = "\n".join(row)
    return "<tr>\n" + row + "\n</tr>"

con = sqlite3.connect("painting.db")
cur = con.cursor()

def get_rows(query):
    cur.execute(query)
    rows = cur.fetchall()
    rows = list(map(prepare_row, rows))
    return "\n".join(rows)

try:
    rows_author = get_rows("SELECT * FROM AUTHOR")
except sqlite3.OperationalError:
    rows_author = ""
try:
    rows_painting = get_rows("SELECT * FROM PAINTING")
except sqlite3.OperationalError:
    rows_painting = ""

print("Content-type: text/html\n")

print(f"""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Painting tables</title>
        </head>
        <body>
        """)

if rows_author:
    print(f"""<h3>Authors</h3>
            <table>
            <thead>
                <tr>
                <td>ID</td>
                <td>FIRST_NAME</td>
                <td>SURNAME</td>
                <td>SEX</td>
                </tr>
            </thead>
            <tbody>
                {rows_author}
            </tbody>
            </table><br>
            """)
        
if rows_painting:
    print(f"""<h3>Pictures</h3>
            <table>
            <thead>
                <tr>
                <td>ID</td>
                <td>PIC_NAME</td>
                <td>CRE_DATE</td>
                <td>GENRE</td>
                <td>MATERIAL</td>
                <td>HEIGHT</td>
                <td>WIDTH</td>
                <td>AUTHOR_ID</td>
                <td>GALLERY_ID</td>
                </tr>
            </thead>
            <tbody>
                {rows_painting}
            </tbody>
            </table><br>
            """)

print("""<form action="/redirect.html">
        <input type="submit" value="Main page">
        </form><br>""")

print("""</body>
        </html>""")

con.close()