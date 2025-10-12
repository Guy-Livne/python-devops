from functools import wraps
import time
import random

# TODO: Define the MaxRetriesExceededError custom exception, accepting `attempts` and `last_exception` as arguments. It should also create a helpful error message to pass to the parent class.

class MaxRetriesExceededError(Exception):
    def __init__(self,attempts,last_exception):
        self.attempts=attempts
        self.last_exception= last_exception
        super().__init__(f" Passed max attempts:{attempts} last_exception was: {last_exception}")

def retry_with_backoff(max_attempts, base_delay=1.0, jitter=0.1):
    
    """
    A decorator factory for retrying a function with validation, exponential
    backoff, jitter, and custom exceptions.
    """
   
    if(max_attempts <= 0):
        raise ValueError("max_attempts must be a positive integer")  
        
    elif(base_delay < 0):
        raise ValueError("base_delay must be a non-negative number")  
        
    elif(jitter < 0):
        raise ValueError("jitter must be a non-negative number")  
   
    
    def decorator(func):
        last_exception = None 
        @wraps(func)
        def wrapper(*args,**kargs):
            
            for i in range(1,max_attempts+1):
                try:
                    return func(*args,**kargs)
                
                except Exception as e:
                    if i == max_attempts:
                        raise MaxRetriesExceededError(i,e) from e 
                        
                    else:
                        last_exception=e 
                        delay = base_delay * (2 ** (i - 1)) + random.uniform(0, jitter)
                        print(f"Attempt {i} failed: {e}. Retrying in {delay:.2f}s...")
                        time.sleep(delay)
                
        
        return wrapper
        
    return decorator
    # TODO: Add validation for the factory's arguments.
    # TODO: Implement the retry logic, storing any exceptions from the decorated function for later use.
    # TODO: On success, return the result immediately.
    # TODO: On failure, store the exception in a suitable variable.
    # TODO: If the maximum attempts are exceeded, raise the appropriate exception, chaining it from the last raised exception.