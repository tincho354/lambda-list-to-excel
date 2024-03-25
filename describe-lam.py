import boto3
import json

def list_lambda_functions():
    lambda_client = boto3.client('lambda')
    return lambda_client.list_functions()['Functions']

def get_function_details(function_name):
    lambda_client = boto3.client('lambda')
    function_details = lambda_client.get_function(FunctionName=function_name)
    return function_details

def identify_environment(function_name, function_details):
    # Aquí puedes agregar la lógica para identificar el ambiente
    # Por ejemplo, basado en el nombre de la función o variables de entorno
    environment = "unknown"  # Modificar esta línea según tu lógica
    return environment

def main():
    lambda_functions = list_lambda_functions()
    all_function_details = []

    for function in lambda_functions:
        details = get_function_details(function['FunctionName'])
        environment = identify_environment(function['FunctionName'], details)
        details['Environment'] = environment
        all_function_details.append(details)

    with open('lambda_functions_details.json', 'w') as file:
        json.dump(all_function_details, file, indent=4, default=str)

if __name__ == "__main__":
    main()
