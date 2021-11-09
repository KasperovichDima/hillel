from flask import Flask,jsonify
from webargs import fields
from webargs.flaskparser import use_kwargs
from sql_module import tracks_length_by_genres,top_sale_tracks
from formater import dict_to_html,lst_to_html


app = Flask(__name__)


@app.errorhandler(400)
@app.errorhandler(422)
def handler_error(err):
    headers=err.data.get('headers')
    messages=err.data.get('messages')
    if headers:
        return jsonify({'errors':messages},err.code,headers)
    else:
        return jsonify({'errors':messages},err.code)


@app.route('/tracks_length_by_genre')
def GetTracksCount():
    """
    Returns total tracks length,
    grouped by genres
    """
    return dict_to_html(tracks_length_by_genres())


@app.route('/top_sale_tracks')
@use_kwargs(
    {
        'count':fields.Int(
            missing='',
            validate=[lambda count: count>0]
        )
    },
    location='query'
)

def TopSaleTracks(count):
    """
    Returns [number] of top saling tracks
    """
    return lst_to_html(top_sale_tracks(count))

app.run(debug=True)