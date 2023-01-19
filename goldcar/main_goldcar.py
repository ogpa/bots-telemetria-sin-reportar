from goldcar.login_goldcar import login_goldcar
from goldcar.focus_reportes import focus_reportes
from goldcar.generar_reporte_horas_trabajadas import generar_reporte_horas_trabajadas
from goldcar.descargar_reporte_horas_trabajadas import descargar_reporte_horas_trabajadas
from goldcar.generar_reporte_kilometraje_y_horas import generar_reporte_kilometraje_y_horas
from goldcar.descargar_reporte_kilometraje_y_horas import descargar_reporte_kilometraje_y_horas
from goldcar.obtener_reporte import crear_csv


def scan_goldcar(hora_reporte):
    sid = login_goldcar()
    focus_reportes(sid)
    # Aquí se coloca el from to de las fechas
    generar_reporte_horas_trabajadas(hora_reporte, sid)
    path_horas_trabajadas = descargar_reporte_horas_trabajadas(sid)
    generar_reporte_kilometraje_y_horas(hora_reporte, sid)
    path_kilometraje_y_horas = descargar_reporte_kilometraje_y_horas(sid)

    df = crear_csv(path_horas_trabajadas,
                   path_kilometraje_y_horas, hora_reporte)

    return df
