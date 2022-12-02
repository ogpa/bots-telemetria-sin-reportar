from poly_regiones import region
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

regiones = region()
x = len(regiones)
x = range(x)
lista_regiones = ["Lima", "Callao", "Arequipa", "La Libertad", "Lambayeque", "Ica", "Ancash", "Piura", "Cusco", "Huanuco", "Junin", "Pasco", "Ayacucho",
                  "Amazonas", "Apurimac", "Cajamarca", "Huancavelica", "Moquegua", "Puno", "San Martin", "Tacna", "Tumbes", "Ucayali", "Madre de Dios", "Loreto"]


def asignar_region(latitud, longitud):
    for n in x:
        if regiones[n].contains(Point(latitud, longitud)):
            break
    return lista_regiones[n]
