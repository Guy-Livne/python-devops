import re

def redact_sensitive_data(content: str) -> str:
    """
    Finds and redacts sensitive values (api_key, password, secret) in a string.

    Args:
        content (str): The string content to be sanitized.

    Returns:
        str: The content with sensitive values replaced by '[REDACTED]'.
    
    Raises:
        TypeError: If content is not a string.
    """
    
    if not isinstance(content,str):
        raise TypeError("'content' must be type str")
        
    
    pattern=r"(?i)(?P<key>api_key|password|secret)(?P<divider>\s*=\s*|\s*:\s*)(?:.+)"
    replacement= r"\g<key>\g<divider>[REDACTED]"
    
    return re.sub(pattern,replacement,content)
    
    
    # TODO: Input validation.
    # TODO: Define a regex that matches the sensitive key-value pairs, as specified in the exercise description.
    # TODO: Define an apply a replacement string.
    # TODO: Return the redacted content.
    