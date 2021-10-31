from requests import get

def bitcoin_rate(currency):
    """
    Returns current Bitcoin rate
    for currency, specified in query.
    """
    data = get('https://bitpay.com/api/rates').json()
    for curr in data:
        if curr['code']==currency:
            curr_name=curr['name']
            curr_rate=curr['rate']
            return f'<h1>Bitcoin rate</h1>' \
                   f'<h3>in {curr_name} is:</h3>' \
                   f'<h2>{curr_rate} {currency}</h2>' \
                   f'<h3>for 1 Bitcoin</h3>'


def valid_list():
    """
    returns a list of currency(code) for query validation
    """
    validation_lst = []
    data = get('https://bitpay.com/api/rates').json()
    for currency in data:
        validation_lst.append(currency['code'])
    return validation_lst

