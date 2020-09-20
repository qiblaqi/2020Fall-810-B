def raise_exception():
    raise ValueError
    print("leaving raise_exception()")

def inner():
    raise_exception()
    print("leaving inner()")

def outer():
    inner()
    print("leaving outer()")

def way_out():
    try:
        outer()
    except ValueError:
        print("way_out(): caught a ValueError")
    print("leaving way_out()")

way_out()