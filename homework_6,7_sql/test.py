import sqlite3


db = sqlite3.connect('example.db')
cursor = db.cursor()
cursor.execute('''SELECT * from genres''')
result_dict = {_[0]:[ _[1],0] for _ in cursor.fetchall()}
cursor.execute('''SELECT GenreId, Milliseconds
               FROM tracks;''')
for GenreId, Milliseconds in cursor.fetchall():
    print(GenreId, Milliseconds)
    # result_dict[track[0]][1] += track[1]

# print(result_dict)
#
# for y,z in result_dict.values():
#     print(y,z)

# from datetime import timedelta
# result = '<h2>Total tracks length by genres:</h2>'
# for genre, mls in result_dict.values():
#     result += f'<b>{genre}</b>: {timedelta(milliseconds=mls)}'
#     result = result.replace(result[result.find('.'):], '<br>')
# print(result)