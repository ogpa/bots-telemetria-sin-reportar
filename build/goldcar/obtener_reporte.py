import requests
import urllib
from datetime import datetime

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os

filename_horas_trabajadas = "/tmp/" + "Horas_Trabajadas.xlsx"
filename_kilometraje_horas = "/tmp/" + "Kilometraje_Horas.xlsx"


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def fecha(delta):
    d = datetime.today() - timedelta(days=delta)
    fecha_ddmmyyyy = d.strftime("%d/%m/%Y")
    return fecha_ddmmyyyy


def convertir_placa(descripcion_vehiculo):
    c = "-"
    pos_guion = descripcion_vehiculo.find(c)
    if pos_guion != -1:
        placa = descripcion_vehiculo[pos_guion-3:pos_guion+4]
    else:
        placa = descripcion_vehiculo
    return placa


def calcular_dias_uso(horas_movimiento):

    if horas_movimiento == 0:
        dias_uso = 0
    elif horas_movimiento > 0:
        dias_uso = 1
    return dias_uso


def calcular_porcentaje_ralenti(movimiento, ralenti):

    if (ralenti == 0):
        porcentaje_ralenti = 0
    else:
        porcentaje_ralenti = (
            ralenti/(movimiento+ralenti))
    return porcentaje_ralenti


def convertir_hhmmss(hhmmss):
    if hhmmss == " :00" or hhmmss == "0":
        hora = 0
    else:
        # Obtener los 3 datos de hh:mm:ss
        h = extraer_texto(hhmmss, "", ":")
        # print(h)
        h = int(h)
        m = extraer_texto(hhmmss, ":", ":")
        # print(m)
        m = int(m)
        s = hhmmss[-2:]
        # print(s)
        s = int(s)
        hora = h + m/60 + s/3600
    return hora


def ayer():
    d = datetime.today() - timedelta(days=1)
    d_p = d.strftime("%Y%m%d")
    d_df = d.strftime("%d/%m/%Y")
    return d_p, d_df


def csv_horas_trabajadas(archivo):
    df = pd.read_excel(archivo, engine="openpyxl", sheet_name="Horas de motor")
    # Reemplazo № para poder usar print
    df = df.rename(
        columns={df.columns[0]: "N", df.columns[1]: "descripcion_vehiculo", "En movimiento": "horas_movimiento", "Detenido": "horas_ralenti"})

    #df.rename(columns={'№': 'N'}, inplace=True)
    # Eliminar "decimales" de columna N
    df = df.drop(df[(df["N"] % 1 != 0)].index)
    df = df.iloc[:, [1, 5, 6]]
    df = df.reset_index(drop=True)
    df["horas_movimiento"] = df.apply(lambda x: convertir_hhmmss(
        x["horas_movimiento"]), axis=1)
    df["horas_ralenti"] = df.apply(lambda x: convertir_hhmmss(
        x["horas_ralenti"]), axis=1)
    df["porcentaje_ralenti"] = df.apply(lambda x: calcular_porcentaje_ralenti(
        x["horas_movimiento"], x["horas_ralenti"]), axis=1)
    df["dias_uso"] = df.apply(
        lambda x: calcular_dias_uso(x["horas_movimiento"]), axis=1)
    df["placa"] = df.apply(
        lambda x: convertir_placa(x["descripcion_vehiculo"]), axis=1)
    df["proveedor"] = "Goldcar"
    fecha_ayer = ayer()
    df["fecha"] = fecha_ayer[1]
    return df


def csv_kilometraje_horas(archivo):
    df = pd.read_excel(archivo, engine="openpyxl",
                       sheet_name="Kilometraje por Viajes")
    df = df.iloc[:, [1, 2, 4]]
    df = df.rename(
        columns={df.columns[0]: "descripcion_vehiculo", df.columns[1]: "distancia", df.columns[2]: "velocidad_maxima"})
    df = df.drop(df[(df["descripcion_vehiculo"] == "Total")].index)
    df["placa"] = df.apply(
        lambda x: convertir_placa(x["descripcion_vehiculo"]), axis=1)
    return df


def crear_csv(filename_horas_trabajadas, filename_kilometraje_horas, hora_reporte):
    df_ht = csv_horas_trabajadas(filename_horas_trabajadas)
    df_kh = csv_kilometraje_horas(filename_kilometraje_horas)
    # return x
    df_goldcar = pd.merge(df_kh, df_ht, on="placa", how="left")
    df_goldcar = df_goldcar.fillna(0)

    df_goldcar = df_goldcar.rename(
        columns={df_goldcar.columns[0]: "descripcion_vehiculo"})

    if hora_reporte == "Ayer":
        fecha_payload = fecha(1)  # dd/mm/yyyy
    elif hora_reporte == "Hoy":
        fecha_payload = fecha(0)  # dd/mm/yyyy

    df_goldcar["fecha"] = fecha_payload
    df_goldcar["proveedor"] = "Goldcar"
    df_goldcar = df_goldcar.drop("descripcion_vehiculo_y", axis=1)
    # print(df_goldcar)
    #filename_csv_goldcar = "goldcar_productividad.csv"
    #df_goldcar.to_csv(filename_csv_goldcar, index=False)
    return df_goldcar


#crear_csv(filename_horas_trabajadas, filename_kilometraje_horas)
