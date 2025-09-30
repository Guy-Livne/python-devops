def validate_server(server: dict) -> bool:
    
    status_temp= server.get('status',"")
   
    name_flag = server.get('name',"") != ""
    region_flag = server.get('region',"") != ""
    status_flag = status_temp == 'active' or status_temp == 'inactive'
    
    return name_flag and region_flag and status_flag
    
    
    
    
    
    """
    Validates a single server dictionary based on a set of rules.

    Rules:
    - Must be a dictionary.
    - Must contain 'name', 'region', and 'status' keys.
    - 'name' and 'region' must be non-empty strings.
    - 'status' must be either 'active' or 'inactive'.

    Args:
        server: A dictionary representing a server.

    Returns:
        True if the server is valid, False otherwise.
    """
    # TODO: Implement the validation logic for a single server.
    # 1. Check if the input is a dictionary.
    # 2. Check for the presence of all required keys.
    # 3. Check the data types and values for 'name', 'region', and 'status'.
    # Return False at the first sign of invalid data.
  

def generate_inventory_report(servers: list[dict]) -> dict:
   
   ans = {}
  
   for server in servers:
       
       if validate_server(server):
           
           if ans.get(server.get("region"),None) == None:
               ans[server.get("region")] = {"active":[] , 'inactive':[]}
           
               (ans.get(server.get('region'))
            def validate_server(server: dict) -> bool:
                """Validate a single server dictionary.

                Rules:
                - Must be a dict.
                - Must contain 'name', 'region', and 'status'.
                - 'name' and 'region' must be non-empty strings.
                - 'status' must be either 'active' or 'inactive'.

                Returns True when all checks pass, False otherwise.
                """
                if not isinstance(server, dict):
                    return False

                name = server.get('name')
                region = server.get('region')
                status = server.get('status')

                if not isinstance(name, str) or not name:
                    return False
                if not isinstance(region, str) or not region:
                    return False
                if status not in ('active', 'inactive'):
                    return False

                return True


            def generate_inventory_report(servers: list[dict]) -> dict:
                """Generate an inventory report grouped by region and status.

                The returned structure is:
                {
                    'region-name': {
                        'active': [<names>],
                        'inactive': [<names>]
                    },
                    ...
                }

                Invalid server entries (per validate_server) are skipped.
                """
                if not isinstance(servers, list):
                    raise TypeError('servers must be a list of dicts')

                report: dict = {}
                for server in servers:
                    if not validate_server(server):
                        def validate_server(server: dict) -> bool:
                            """Validate a single server dictionary.

                            Rules:
                            - Must be a dict.
                            - Must contain 'name', 'region', and 'status'.
                            - 'name' and 'region' must be non-empty strings.
                            - 'status' must be either 'active' or 'inactive'.

                            Returns True when all checks pass, False otherwise.
                            """
                            if not isinstance(server, dict):
                                return False

                            name = server.get('name')
                            region = server.get('region')
                            status = server.get('status')

                            if not isinstance(name, str) or not name:
                                return False
                            if not isinstance(region, str) or not region:
                                return False
                            if status not in ('active', 'inactive'):
                                return False

                            return True


                        def generate_inventory_report(servers: list[dict]) -> dict:
                            """Generate an inventory report grouped by region and status.

                            The returned structure is:
                            {
                                'region-name': {
                                    'active': [<names>],
                                    'inactive': [<names>]
                                },
                                ...
                            }

                            Invalid server entries (per validate_server) are skipped.
                            """
                            if not isinstance(servers, list):
                                raise TypeError('servers must be a list of dicts')

                            report: dict = {}
                            for server in servers:
                                if not validate_server(server):
                                    continue

                                region = server['region']
                                status = server['status']  # 'active' or 'inactive'
                                name = server['name']

                                report.setdefault(region, {'active': [], 'inactive': []})
                                report[region][status].append(name)

                            return report


                        if __name__ == '__main__':
                            # Small demo / smoke test
                            sample = [
                                {'name': 'web-01', 'region': 'us-east', 'status': 'active'},
                                {'name': 'db-01', 'region': 'us-east', 'status': 'inactive'},
                                {'name': '', 'region': 'eu', 'status': 'active'},  # invalid
                                {'name': 'cache-01', 'region': 'eu', 'status': 'active'},
                            ]

                            from pprint import pprint
                            pprint(generate_inventory_report(sample))
