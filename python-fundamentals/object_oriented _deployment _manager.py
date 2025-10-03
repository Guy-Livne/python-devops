class Deployment:
    """
    Manages the state and version history of a software deployment.
    """

    def __init__(self, service_name: str, environment: str):
        self.service_name = service_name
        self.environment = environment
        self.status = 'pending'
        self.version = None
        self.prev_versions = []

    def deploy(self, new_version: str):
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