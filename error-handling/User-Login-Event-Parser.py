import re
from typing import Optional

def parse_login_event(log_line: str) -> Optional[dict[str, str]]:
    """
    Parses a login event log line to extract the username and status.

    Args:
        log_line (str): The log line to parse.

    Returns:
        A dictionary with 'username' and 'status' if the line matches,
        otherwise None.
        
    Raises:
        TypeError: If log_line is not a string.
    """
    
    if not isinstance(log_line,str):
        raise TypeError("'log_line' must be type str")
        
        
    ans= None 
    match= re.search(r"^LOGIN_EVENT: User '(?P<username>\w+)' login attempt was (?P<status>\w+)\.$",log_line)
    
    if match:ans={"username":match.group("username"),"status":match.group("status")}
    
    return ans
    
    
    
    # TODO: Input validation
    
    # TODO: Define a regular expression pattern to match the log format:
    # "LOGIN_EVENT: User '{username}' login attempt was {status}."
    
    # TODO: If a match is found, return the dictionary of named groups; otherwise, return None.
    