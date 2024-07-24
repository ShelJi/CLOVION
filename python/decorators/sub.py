def swapper_dec(func):
    def wrapper(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)
    return wrapper

@swapper_dec
def sub(a,b):
    print(a-b)

sub(5,10)

