def read_log_lines(filepath):
    
    with open(filepath) as file:
        
        for line in file:
           
            if not line.strip().startswith('#') and line.strip() != "" :
                yield line.strip()
        
        
    
    
    
    """
    Creates a generator that reads a log file, yielding valid, non-comment lines.

    Args:
        filepath (str): The path to the log file.

    Yields:
        str: A stripped, non-empty, non-comment line from the file.
    """
    # TODO: Implement the generator logic.
    # 1. Open the file safely.
    # 2. Iterate through each line, removing whitespace and checking whether it's valid.
    # 3. If the line is valid, yield it.
    pass
