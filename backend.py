import sqlite3

def conn(list):
    conn=sqlite3.connect("properties.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS property (id INTEGER PRIMARY KEY,location TEXT, price INTEGER, size TEXT)")
    for dict in list:
        if type(dict["price"]) is None:
            None
        try:
            location,price,size=dict["location"],dict["price"],dict["size"]
            cur.execute("INSERT INTO property VALUES (NULL,?,?,?)",(location,int(price),size))
        except:
            location,price,size=dict["location"],dict["price"],dict["size"]
            cur.execute("INSERT INTO property VALUES (NULL,?,?,?)",(location,price,size))

    conn.commit()
    conn.close

#inserts all the properties

def viewAll():
    conn=sqlite3.connect("properties.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM property")
    rows=cur.fetchall()
    conn.close()
    return rows
    
def search(location=""):
    conn=sqlite3.connect("properties.db")
    cur = conn.cursor()
    if location == "":
        cur.execute("SELECT * FROM property")
    else:
        cur.execute("SELECT * FROM property WHERE location=?",(location,))
    rows=cur.fetchall()
    conn.close()
    return rows
    
def filter(dmin,dmax):
    conn=sqlite3.connect("properties.db")
    cur = conn.cursor()
    try:
        min = int(dmin)
    except:
        min = 0
    try:
        max = int(dmax)
    except:
        max = 100000
    cur.execute("SELECT * FROM property WHERE price BETWEEN ? AND ?",(min,max))
    rows=cur.fetchall()
    conn.close()
    return rows
    

