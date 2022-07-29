import sqlite3


def conn(list):
    conn=sqlite3.connect("properties.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS property")
    cur.execute("CREATE TABLE IF NOT EXISTS property (id INTEGER PRIMARY KEY,location TEXT, price INTEGER, size TEXT, link TEXT)")
    for dict in list:
        if dict["link"] is None:
            None
        else:
            try:
                location,price,size,link=dict["location"],dict["price"],dict["size"],dict["link"]
                cur.execute("INSERT INTO property VALUES (NULL,?,?,?,?)",(location,int(price),size,link))
            except:
                location,price,size,link=dict["location"],dict["price"],dict["size"],dict["link"]
                cur.execute("INSERT INTO property VALUES (NULL,?,?,?,?)",(location,price,size,link))
        
    conn.commit()
    conn.close
    
def viewAll(location,dPriceMin,dPriceMax):
    conn=sqlite3.connect("properties.db")
    cur = conn.cursor()
    try:
        PriceMin = int(dPriceMin)
    except:
        PriceMin = 0
    try:
        PriceMax = int(dPriceMax)
    except:
        PriceMax = 100000
    non = "neuvedena"
    
    #both categories unfilled / price filled
    if location == "":
        cur.execute("SELECT id, location, price, size FROM property WHERE price BETWEEN ? AND ? OR price = ?",(PriceMin,PriceMax,non))
    #both categories filled
    else:
        cur.execute("SELECT id, location, price, size FROM property WHERE location=? AND price BETWEEN ? AND ?",(location,PriceMin,PriceMax))

    rows=cur.fetchall()

    #space outs all of the items items
    spacedRows = []
    for row in rows:
        spacedRow = []
        for index,item in enumerate(row):
            item = str(item).strip()
            print(len(max([str(item[index]) for item in rows],key=len)) - len(str(row[index]).strip()))
            print()
            print(f"item {item}")
            spacing = (len(max([str(item[index]) for item in rows],key=len)) - len(str(row[index]).strip()))
            space = " "
            spacedRow.append(f"{item}{spacing * space}")
        spacedRows.append(spacedRow)
        
    return spacedRows


    

