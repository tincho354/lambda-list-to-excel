# process-data.py

import pandas as pd
import json

def load_lambda_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    processed_data = []
    for function in data:
        function_info = {
            'Function Name': function['Configuration']['FunctionName'],
            'Runtime': function['Configuration']['Runtime'],
            'Memory Size': function['Configuration']['MemorySize'],
            'Timeout': function['Configuration']['Timeout'],
            'Environment': function.get('Environment', 'Unknown'),
            'IAM Role': function['Configuration']['Role'],
            'Last Modified': function['Configuration']['LastModified']
        }
        # Añadir más campos según sea necesario
        processed_data.append(function_info)
    return processed_data

def process_lambda_data():
    lambda_data = load_lambda_data('lambda_functions_details.json')
    processed_lambda_data = process_data(lambda_data)
    df = pd.DataFrame(processed_lambda_data)
    
    # Guardar en un archivo Excel
    df.to_excel('processed_lambda_data.xlsx', index=False)

if __name__ == "__main__":
    process_lambda_data()
