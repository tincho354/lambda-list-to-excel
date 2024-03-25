import boto3
import pandas as pd

def list_lambda_functions(lambda_client):
    functions = []
    paginator = lambda_client.get_paginator('list_functions')
    
    for page in paginator.paginate():
        functions.extend(page['Functions'])

    return functions

def get_event_source_mappings(lambda_client, function_name):
    event_sources = []
    paginator = lambda_client.get_paginator('list_event_source_mappings')

    for page in paginator.paginate(FunctionName=function_name):
        event_sources.extend(page['EventSourceMappings'])

    return event_sources

def main():
    lambda_client = boto3.client('lambda')
    functions = list_lambda_functions(lambda_client)

    lambda_details = []

    for function in functions:
        function_name = function['FunctionName']
        event_source_mappings = get_event_source_mappings(lambda_client, function_name)

        lambda_details.append({
            "Function Name": function_name,
            "Runtime": function['Runtime'],
            "Memory Size": function['MemorySize'],
            "Environment Variables": function.get('Environment', {}).get('Variables', {}),
            "Role": function['Role'],
            "Last Modified": function['LastModified'],
            "Event Source Mappings": event_source_mappings,
            "VPC": function.get('VpcConfig', {}).get('VpcId', ''),
            "Subnets": function.get('VpcConfig', {}).get('SubnetIds', [])
        })

    df = pd.DataFrame(lambda_details)
    df.to_excel('lambda_function_details.xlsx', index=False)

if __name__ == "__main__":
    main()
