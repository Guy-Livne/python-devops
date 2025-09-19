def parse_log_line(log_line: str) -> dict | None:
    
    ans={}
    
    if log_line != None and log_line != "" and type(log_line) == str:
        log_list = log_line.split(" ", 2)
        
        ans["timestamp"]= log_list[0]
        ans["message"]= log_list[2] if len(log_list) > 2 else ""
        
        if (log_list[1].startswith('[')
        and log_list[1].endswith(']') 
        and ans.get("message","") !=""):
            
             ans["log_level"] = log_list[1].strip('[]')
             return ans
            
    return None
  
   
   
    """
    Parses a single log line into a structured dictionary.

    The expected log format is: "TIMESTAMP [LOG_LEVEL] MESSAGE"
    Example: "2024-05-20T13:45:10Z [INFO] User 'alice' logged in successfully."

    Args:
        log_line: A string representing a single line from a log file.

    Returns:
        A dictionary containing the 'timestamp', 'log_level', and 'message'
        if the log line is valid, otherwise None.
    """
    # TODO: Implement the parsing logic here.
    # 1. Check if the log_line is valid. If not, return None.
    # 2. Split the line into its constituent parts: timestamp, log_level, and message.
    #    Remember that the message itself can contain spaces.
    # 3. Clean up the log_level to remove the square brackets.
    # 4. Create and return a dictionary with the extracted parts.
    pass