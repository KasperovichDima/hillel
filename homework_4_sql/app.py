from flask import Flask
from sql_module import tracks_count,unique_name
from formater import count_to_html

app = Flask(__name__)

@app.route('/tracks_count')
def get_tracks_count():
    """
    Returns the number of records from table `Tracks`
    """
    return count_to_html(tracks_count())


@app.route('/unique_name')
def get_unique_name():
    """
    Returns the number of unique records in
    column FirstName from table `customers`
    """
    return count_to_html(unique_name())

app.run(debug=True)