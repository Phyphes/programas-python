# Módulos integrados en python que se pueden importar

import os ; import sys
import datetime, calendar
# Algunas funciones del modulo os de python
os.system('cls')
print(f'\nSistema operativo: \n{sys.platform}')
print(f'\nDirectorio actual: \n{os.getcwd()}')
print('\nListado de archivos en el directorio raiz:')
os.chdir('/')
print(os.listdir())
print('\nVariables de entorno: ')
print(os.environ)
print(f"\nRuta de ejecucion : \n{os.getenv('PATH')}")
# Algunas funciones del modulo datetime
ahora = datetime.datetime.now()
print('\nLa fecha y hora actuales:', ahora)
print('\nLa fecha actual :', ahora.strftime('%b / %d / %Y'))
print('\nLa hora actual :', ahora.strftime('%H:%M'))
# Algunas funciones del modulo calendar
print('\nCalendario 2023: \n')
calendar.prcal(2023)
print('\nMes noviembre 2023: \n')
calendar.prmonth(2023,11)