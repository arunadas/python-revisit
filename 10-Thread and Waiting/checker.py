from flask import session
from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:    
            return func(*args, **kwargs)
        return 'You are NOT logged in.'   
    return wrapper  


    
# 1. code to execute BEFORE calling the decorated function. 
# 2. call the decorated function as required, returning its results if needed. 
# 3. Code to execute INSTEAD of calling the decorated function.     