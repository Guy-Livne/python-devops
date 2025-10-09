from functools import wraps

def require_role(required_role):
    """
    A decorator factory that creates a decorator to check for a specific user role.

    Args:
        required_role (str): The role string that the user must have.

    Returns:
        A decorator function.
    """
    def decorator(func):
        @wraps(func)
        def warpper(*args,**kargs):
            roles_list = kargs['user'].get("roles",[])
            if required_role in roles_list:
                return func(*args,**kargs)
            else:
                raise PermissionError
                
        return warpper
    return decorator