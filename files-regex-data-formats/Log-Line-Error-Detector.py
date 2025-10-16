import re

def has_critical_error(log_line: str) -> bool:
    """
    Checks if a log line contains a critical error indicator ('ERROR:' or 'FAIL:').
    The check is case-insensitive.

    Args:
        log_line (str): The log line to check.

    Returns:
        bool: True if a critical error indicator is found, False otherwise.
    """
    if not isinstance(log_line,str):
        raise TypeError("'log_line' must be type str")
        
    return bool(re.search(r"ERROR:|FAIL:",log_line,re.I))