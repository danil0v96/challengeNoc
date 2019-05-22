# Challenge NOC

# Tecnologías utilizadas:

- Python 3.3+
- Boto3 (Package)
  Boto es un paquete de Python que proporciona interfaces para AWS, incluido Amazon S3.
- AWS Cli

# Instalación del paquete "boto3" y "AWS Cli":

$ pip install boto3
$ pip install awscli --upgrade

# Configurando las credenciales de AWS:

Para poder utilizar la SDK y conectarnos con la cuenta de Amazon, es necesario proveer las credenciales. Esto lo podemos hacer con el comando interactivo de AWS Cli:

$ aws configure
AWS Access Key ID [None]: clave-de-acceso
AWS Secret Access Key [None]: clave-secreta
Default region name [None]: sa-east-1
Default output format [None]: json

# Script:

La carga y descarga de archivos se hace mediante 2 funciones propias de boto3: 
- s3_client.download_file(bucketName, path, saveName)
- s3_client.upload_file(path, bucketName, outputName)

La variable "bucketName" está hardcodeada ya que sería el único bucket al que vamos a subir archivos, pero adentro de cada función está comentado un input en el caso de que se necesite especificar el nombre de otro bucket en el que queremos descargar/subir un archivo.

# Sincronización del Bucket S3 con la instancia EC2:

Cada 5' se ejecuta un archivo crontab, el cual ejecuta un script para hacer la sincronización con el comando "aws s3 sync" de AWS Cli.

Esto permite que se descarguen todos los archivos nuevos o aquellos que hayan sido modificados.




  
