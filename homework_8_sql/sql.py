import sqlite3


def tracks_length_by_genres():
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    cursor.execute('''SELECT 
    g.Name, SUM(t.Milliseconds) 
    FROM tracks t JOIN genres g 
    ON t.GenreId = g.GenreId 
    GROUP BY g.Name;''')

    res=cursor.fetchall()
    db.close()
    return res




def top_sale_tracks(count):
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    sql=('''SELECT 
    t.Name, SUM(ii.UnitPrice * ii.Quantity) as summa 
    FROM tracks t LEFT JOIN invoice_items ii 
    ON t.TrackId = ii.TrackId 
    GROUP by t.TrackId 
    ORDER BY summa DESC''')

    if count:
        sql+=f" LIMIT {count}"

    cursor.execute(f"{sql}")

    res=cursor.fetchall()
    db.close()

    return res