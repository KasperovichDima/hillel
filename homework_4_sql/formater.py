def count_to_html(res):
    return f'<h2>number of records <br>' \
           f'<h1>{res}</h1>'

def lst_to_html(res):
    res_lst = [_[0] for _ in res]
    res_str = '<br>'.join(res_lst)
    return f"<h2>Unique names:</h2>" \
           f"'{res_str}"