import boto3
import pandas as pd

# Función para obtener datos de instancias EC2
def obtener_datos_ec2():
    # Crear un cliente EC2
    ec2 = boto3.client('ec2')

    # Obtener información sobre todas las instancias EC2
    instancias = ec2.describe_instances()
    datos_instancias = []

    # Recorrer las instancias y extraer la información deseada
    for reserva in instancias['Reservations']:
        for instancia in reserva['Instances']:
            datos_instancias.append({
                'InstanceID': instancia['InstanceId'],
                'Tipo': instancia['InstanceType'],
                'Estado': instancia['State']['Name'],
                'AMI': instancia['ImageId'],
                # Puedes agregar más campos según sea necesario
            })

    return datos_instancias

# Función para exportar a Excel
def exportar_a_excel(datos, nombre_archivo):
    df = pd.DataFrame(datos)
    df.to_excel(nombre_archivo, index=False)

# Uso de las funciones
datos_ec2 = obtener_datos_ec2()
exportar_a_excel(datos_ec2, 'informacion_ec2.xlsx')
