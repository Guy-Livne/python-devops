import subprocess
import sys

def check_host_status(hostname: str) -> str:
    """
    Checks if a host is online by pinging it a limited number of times.

    Args:
        hostname (str): The hostname or IP address to ping.

    Returns:
        'online' if the host is reachable (ping exit code 0), 'offline' otherwise.
    
    Raises:
        TypeError: If hostname is not a string.
        ValueError: If hostname is not a non-empty string.
    """
    
    if not isinstance(hostname,str):
        raise TypeError(f"'hostname' must me type str , hostname current type {type(hostname)}")
        
    if hostname == "":
        raise ValueError("'hostname' must be a non-empty string")
        
    ans = None     
    cmd=["ping","-c","3",hostname]
    try:
        result = subprocess.run(cmd,
        timeout=5,
        check=True, 
        cupture_output=True, 
        text=True)
        
        ans ="online" if result.returncode == 0 else "offline"
        
    except subprocess.TimeoutExpired as e:
        ans="offline"
    
    return ans
        
 
        
    
        
    # TODO: Input validation
    # TODO: Construct and run the ping command. Make sure that subprocess does not raise an exception on non-zero exit codes.
    # TODO: Handle relevant exceptions.
    # TODO: Return "online" or "offline" according to the exercise description.
    pass