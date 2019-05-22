import boto3

s3_client = boto3.client('s3') #Conexión a AWS
bucketName = "nocsupport-fury"

def subirArchivoS3():

    val = input("S/N: ")

    while (val == "S"):
        #bucketName = input("Ingrese el nombre del bucket en el cual desea subir el archivo:   ")
        path = input("Ingrese la ruta del archivo que desea subir:  ")
        outputName = input("Ingrese el nombre con el que desea guardar el archivo en el bucket:  ")
        try:
            s3_client.upload_file(path, bucketName, outputName)
        except:
            print("No se pudo subir el archivo")
        else:
            print("Carga finalizada")

        val = input("¿Desea seguir cargando archivos a un bucket? S/N:   ")


def descargarArchivoS3():

    val = input("S/N: ")

    while (val == "S"):
        #bucketName = input("Ingrese el nombre del bucket del cual desea descargar el archivo:   ")
        path = input("Ingrese la ruta del archivo que desea descargar:  ")
        saveName = input("Ingrese el nombre con el que desea guardar el archivo:  ")
        try:
            s3_client.download_file(bucketName, path, saveName)
        except:
            print("No se pudo subir el archivo")
        else:
            print("Descarga finalizada")

        val = input("¿Desea seguir cargando archivos al bucket? S/N:   ")

if __name__ == "__main__":

    print("¿Cargar un archivo a un bucket?")
    subirArchivoS3()
    print("¿Descargar un archivo desde un bucket?")
    descargarArchivoS3()


