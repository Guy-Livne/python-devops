class Deployment:
    """
    Manages the state and version history of a software deployment.
    """

    def __init__(self, service_name: str, environment: str):
        if not isinstance(service_name, str) or not isinstance(environment, str):
            raise TypeError("'service_name' and 'environment' must be type 'str'")
                
        elif service_name == "" or environment == "":
            raise ValueError("'service_name' and 'environment' must be non-empty strings")
       
        self.service_name = service_name
        self.environment = environment
        self.status = 'pending'
        self.version = None
        self.prev_versions = []

    def deploy(self, new_version: str):
        if not isinstance(new_version, str):
            raise TypeError("'new_version' must be 'str'")
            
        elif new_version == "":
            raise ValueError("'new_version' must be a non-empty string")

        
        self.status = 'deployed'
        self.prev_versions.append(self.version)
        self.version= new_version
        

    def rollback(self) -> bool:
        if len(self.prev_versions) > 1:
            # TODO: write code...
            prev_version = self.prev_versions.pop()
            self.version= prev_version
            self.status='rolled_back'
            return True
            
    
        return False
            

    def check_status(self) -> dict:
        ans ={'service_name':self.service_name, 'environment':self.environment, 'status':self.status, 'version':self.version}
        return ans