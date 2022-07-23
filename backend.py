import sqlite3

def conn(list):
    conn=sqlite3.connect("properties.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS property")
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
    
def search(location,dmin,dmax):
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
    non = "neuvedena"
    #both categories unfilled / price filled
    if location == "":
        cur.execute("SELECT * FROM property WHERE price BETWEEN ? AND ? OR price = ?",(min,max,non))
    #both categories filled
    else:
        cur.execute("SELECT * FROM property WHERE location=? AND price BETWEEN ? AND ? or price = ?",(location,min,max,non))

    rows=cur.fetchall()
    conn.close()
    return rows


    

