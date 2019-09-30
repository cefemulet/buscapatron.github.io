# buscapatron.github.io
Busca un patrón en una cadena

Busca en un archivo log o cualquier tipo de archivo,
la cadena error o warning mostrando en pantalla el resultado de la busqueda.

Requerimientos:
version de python 3, GNU/Linux

Metodo de ejecucion:

$ python buscaPatron.py /var/log/syslog  # cualquier archivo log 

$ python buscaPatron.py syslog           # si es una copia y la misma esta en el directorio actual

$ chmod 755 buscaPatron.py y luego ./buscaPatron.py /var/log/kern.log
