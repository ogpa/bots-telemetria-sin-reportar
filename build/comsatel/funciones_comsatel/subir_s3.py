import boto3
S3_BUCKET_NAME = "apps-mbr"
S3_RUTA_FOLDER = "bi-telemetria/productividad/historico/"


def subir_s3(ruta_consolidado):

    s3 = boto3.client("s3")
    nombre_s3 = S3_RUTA_FOLDER + ruta_consolidado
    with open(ruta_consolidado, "rb") as f:
        s3.upload_fileobj(f, S3_BUCKET_NAME, nombre_s3)
    # return x
