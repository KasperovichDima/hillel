import sqlite3


def tracks_length_by_genres():
    """
    Creates a dictionary {GenreId: [GenreName, time = 0]}
    Adds and fills the duration for each element of the
    dictionary based on the SQL query
    :return: dict {id:[name,time]}

    """
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    cursor.execute('''SELECT * from genres''')
    result_dict = {_[0]: [_[1], 0] for _ in cursor.fetchall()}

    cursor.execute('''SELECT GenreId, Milliseconds
                   FROM tracks;''')
    for GenreId, Milliseconds in cursor.fetchall():
        result_dict[GenreId][1] += Milliseconds

    db.close()
    return result_dict




def top_sale_tracks(count):
    """
    Creates a dictionary {TrackId: [TrackName, sum = 0]}
    Summarizes and fills in the sales amount for each
    track based on the SQL query
    :param count: results number
    :return:[[track_1_name,track_1_sum],etc...]
    """
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    cursor.execute('''SELECT TrackId, Name from tracks''')
    id_name_sum_dict = {_[0]: [_[1], 0] for _ in cursor.fetchall()}

    cursor.execute('''SELECT TrackId, UnitPrice, Quantity
                       FROM invoice_items;''')
    for TrackId, UnitPrice, Quantity in cursor.fetchall():
        id_name_sum_dict[TrackId][1] += UnitPrice * Quantity

    db.close()

    result_unsorted = [tpl[1] for tpl in id_name_sum_dict.items()]

    if count:
        return sorted(result_unsorted, key=lambda _: _[1], reverse=True)[:count]
    else:
        return sorted(result_unsorted, key=lambda _: _[1], reverse=True)