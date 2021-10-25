from functools import wraps

def report(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        print(f'Function {func.__name__} completed successfully. List generated:')
        return res

    return wrapper


@report
def lst_gen(el_num):
    """
    Generates and returns a list of even numbers.
    The accepted argument specifies the range.
    """
    return [x for x in range(el_num) if x % 2 == 0]


print(lst_gen(500))

