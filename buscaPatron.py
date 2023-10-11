#!/usr/bin/python
"""
Busca en un archivo log o cualquier tipo de archivo la cadena error o warning,
mostrando en pantalla el resultado de la busqueda.

Requerimientos:
version de python 3, GNU/Linux

Metodo de ejecucion:
    $ python buscaPatron.py /var/log/syslog  # cualquier archivo log 
    $ python buscaPatron.py syslog           # si es una copia y la misma esta en el directorio actual
    $ chmod 755 buscaPatron.py y luego ./buscaPatron.py /var/log/kern.log


Cualquier modificacion o mejora seran bienvenidos: cefe.mulet@gmail.com.

"""

def mi_funcion():
    import sys
    import re
    import os 
    pattern = re.compile("[Ee]rror")
    pattern2 = re.compile("[Ww]arn*")

    with open(str(sys.argv[1]),'r') as f:
        for busqueda in f:
            if pattern.search(busqueda):
                print(busqueda)
            else:
                if pattern2.search(busqueda):
                    print(busqueda)

if __name__=='__main__':
    mi_funcion()

