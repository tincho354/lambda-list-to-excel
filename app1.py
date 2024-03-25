import boto3
import pandas as pd

def list_lambda_functions(lambda_client):
    return lambda_client.list_functions()['Functions']

def get_event_source_mappings(lambda_client, function_name):
    return lambda_client.list_event_source_mappings(FunctionName=function_name)['EventSourceMappings']

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

