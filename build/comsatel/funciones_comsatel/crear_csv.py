import requests
import urllib
from datetime import datetime

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os

#ruta_archivo_excel = "27122022_Consolidado_Comsatel.xlsx"


def convertir_placa(descripcion_vehiculo):
    longitud = len(descripcion_vehiculo)
    if longitud == 6:
        placa = descripcion_vehiculo[0:3] + "-" + descripcion_vehiculo[-3:]
    else:
        placa = descripcion_vehiculo
    return placa


def convertir_dias_uso(horas_movimiento):

    if horas_movimiento == 0:
        dias_uso = 0
    elif horas_movimiento > 0:
        dias_uso = 1
    return dias_uso


def convertir_porcentaje_ralenti(horas_movimiento, horas_ralenti):

    if horas_ralenti == 0:
        porcentaje_ralenti = 0
    else:
        porcentaje_ralenti = horas_ralenti/(horas_movimiento + horas_ralenti)
    return porcentaje_ralenti


def ayer():
    d = datetime.today() - timedelta(days=1)
    d_p = d.strftime("%Y%m%d")
    d_df = d.strftime("%d/%m/%Y")
    return d_p, d_df


def crear_csv(archivo_excel):
    df = pd.read_excel(archivo_excel, engine="openpyxl")
    df = df[9:]
    df.columns = df.iloc[0]

    # Extrar solo las columnas necesarias. Empiezan desde 0 (cero)
    # 1 Placa
    # 8 Distancia
    # 12 Horas movimiento trabajo
    # 16 Horas Ralentí
    # 23 velocidad máxima
    # Días de uso = Si 12 > 0
    # % ralenti = 16/(16+12)

    df = df[1:].iloc[:, [1, 8, 12, 16, 23]]

    # 1 8 12 16 23 pasan a ser 0, 1, etc
    # Cambiar nombre de columnas
    df = df.rename(
        columns={df.columns[0]: "descripcion_vehiculo", df.columns[1]: "distancia", df.columns[2]: "horas_movimiento", df.columns[3]: "horas_ralenti", df.columns[4]: "velocidad_maxima"})

    df = df.reset_index(drop=True)
    df["distancia"] = df["distancia"].astype(float)
    df["horas_movimiento"] = df["horas_movimiento"].astype(float)
    df["horas_ralenti"] = df["horas_ralenti"].astype(float)
    df["velocidad_maxima"] = df["velocidad_maxima"].astype(int)

    # Crear columna "placa"
    df["placa"] = df.apply(lambda x: convertir_placa(
        x["descripcion_vehiculo"]), axis=1)

    # Crear columna "dias_uso"
    df["dias_uso"] = df.apply(
        lambda x: convertir_dias_uso(x["horas_movimiento"]), axis=1)

    # Crear columna "porcentaje_ralenti"
    df["porcentaje_ralenti"] = df.apply(lambda x: convertir_porcentaje_ralenti(
        x["horas_movimiento"], x["horas_ralenti"]), axis=1)
    df["proveedor"] = "Comsatel"
    fecha_ayer = ayer()
    df["fecha"] = fecha_ayer[1]
    #nombre_csv = "comsatel_productividad.csv"
    #df.to_csv(nombre_csv, index=False)
    # print(df)
    return df


# crear_csv(ruta_archivo_excel)
