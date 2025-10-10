from functools import wraps

# TODO: Define the AuthorizationError custom exception.
# It should inherit from Exception.
# Its __init__ method should accept `user_name` and `required_role`.
# It should store these as attributes and create a descriptive error message to pass to the parent class's __init__

class AuthorizationError(Exception):
    
    def __init__(self,user_name,required_role):
        self.user_name=user_name
        self.required_role=required_role
        super().__init__(f"User '{user_name}' lacks the required role: '{required_role}'.")

        

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
            
            if (not 'user' in kargs.keys()
            or not isinstance(kargs['user'],dict)
            or not 'roles' in kargs['user'].keys()
            or not isinstance(kargs['user'].get("roles",None),list)):
                raise ValueError("A 'user' keyword argument is required")
                
            roles_list = kargs['user'].get("roles",[])
            
            if required_role in roles_list:
                return func(*args,**kargs)
            else:
                raise AuthorizationError(kargs['user'].get('name',""),required_role)
                
        return warpper
    return decorator
