from datetime import datetime

fecha = "2024-01-16T21:15:41.337Z"
fecha_str = str(fecha)
fecha_obj = datetime.strptime(fecha_str,'%Y-%m-%dT%H:%M:%S.%fZ')
print ("The type of the date is now",  type(fecha_obj))
print ("The date is", fecha_obj)