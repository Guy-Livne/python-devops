
def validate_config(config: dict) -> bool:
    
   required_keys = {"service_name","env","port"}
   set_keys = set(config.keys())
   
   keys_flag = set.difference(required_keys,set_keys) == set()
   
   env_value_flag = (config.get("env",None) == 'dev' or config.get("env",None) =='staging' or config.get("env",None) == 'prod')
   
   ser_name =config.get("service_name","")
   service_name_flag = isinstance(ser_name,str) and ser_name!=""
   
   port_val= config.get("port",0)
   port_flag= isinstance(port_val,int) and  port_val >= 1 and port_val <= 65535
   
    
   
   return keys_flag and env_value_flag and service_name_flag and port_flag
   

   

 # TODO: Implement the validation logic here.
    # 1. Check if all required keys exist.
    # 2. Check if the 'env' value is one of the allowed environments.
    # 3. Check if 'service_name' is a non-empty string.
    # 4. Check if 'port' is an integer and within the valid range.
    # Remember to return False as soon as a check fails.
    # If all checks pass, return True at the end.
    #check if all required keys exist