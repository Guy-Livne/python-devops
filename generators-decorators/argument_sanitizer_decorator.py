import functools
def sanitize_hostname(func):
    """
    A decorator that finds a 'hostname' keyword argument, sanitizes it
    (lowercase, stripped whitespace), and passes it to the wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args,**kargs):
        val = kargs.get("hostname","")
        if val != "" :
            kargs["hostname"]= val.lower().strip()
            ans = func(*args,**kargs)
            return ans
            
    return wrapper
        