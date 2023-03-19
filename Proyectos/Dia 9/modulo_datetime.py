import datetime
from datetime import datetime
from datetime import date
mi_dia = datetime.now()
fecha_nacimiento = date(2000,6,14)
vide = mi_dia.date() - fecha_nacimiento
print(f"Hoy es {mi_dia.strftime('%A, %d de %B de %Y')} y son las: {mi_dia.time()}")
print(f"Los dias que he vivido hasta ahora son {vide.days}")

'''
Práctica Módulo Datetime 1
Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
'''
mi_fecha = date(1999,2,3)

'''
Práctica Módulo Datetime 2
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
'''
hoy = date.today()
print(hoy)

'''
Práctica Módulo Datetime 3

En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe 
almacenar el valor 43
'''
minutos = datetime.now().minute
print(minutos)