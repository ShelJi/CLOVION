# args -> arguments
# kwargs -> keyword arguments


def add(*args):
    
    print(args)

    a = args[0]
    b = args[1]
    print(a+b)

    res = 0
    for i in args:
        res += i

    return res

# print(add(10,10,10, 10))

def addd(**kwargs):
    print(kwargs)

    a = kwargs.get("a")
    b = kwargs.get("b")

    username = kwargs.get("username")

    if username is None:
        raise ValueError("Username is required.")
    
    return f"hello {username}"

print(addd(a=1, b=2, username = "ancy"))