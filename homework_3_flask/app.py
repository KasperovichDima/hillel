from flask import Flask,jsonify
from webargs import fields
from webargs.flaskparser import use_kwargs
from utils import bitcoin_rate, valid_list

app = Flask(__name__)

@app.errorhandler(400)
@app.errorhandler(422)
def handel_error(err):
    headers=err.data.get('headers')
    messages=err.data.get('messages')
    if headers:
        return jsonify({'errors':messages},err.code,headers)
    else:
        return jsonify({'errors':messages},err.code)

<<<<<<< HEAD

=======
>>>>>>> 5d773cf448dccb054f31d383dd065e0ee143b2c1
@app.route('/')
@use_kwargs(
    {
        'currency':fields.Str(
            missing='USD',
<<<<<<< HEAD
            validate=[lambda currency: currency in valid_list()]
=======
            validate=[lambda currency: currency in curr_list()]
>>>>>>> 5d773cf448dccb054f31d383dd065e0ee143b2c1
        )
    },
    location='query'
)
def get_bitcoin_rate(currency):
    """
    Returns current Bitcoin rate
    for currency, specified in query
    """
    return bitcoin_rate(currency)

app.run(debug=True)


