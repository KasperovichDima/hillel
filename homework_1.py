from functools import wraps

def report(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        print(f'Function {func} completed successfully. List generated:')
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
print(lst_gen.__doc__)




def decorator(dec_arg1,dec_arg_2)
    def outer(func):
        def inner(*args,**kwargs):
            do something with dec_arg1
            return func(*args,**kwargs)
            do something with dec_arg_2
        return inner
    return outer

@decorator(dec_arg1,dec_arg_2)
def main_func(arg):
    do something with arg



