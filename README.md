# Data-analytics-challenge
## Descripción
El proyecto descarga 3 archivos en formato .csv desde el data set del ministerio de cultura (https://datos.cultura.gob.ar/dataset), los cuales almacenan los datos de bibliotecas populares, museos y centros culturales. Estos archivos son leídos, y guardados en tablas diferentes en una base de datos PostgreSQL, luego estos se normalizan para almacenarlos en una sola tabla.

## Configuracion
#### Primero deberás crear un entorno virtual, y ejecutarlo. Luego instalar los requerimientos con:
> 	pip install -r requirements.txt

#### Crear un archivo *".env"*  en la raíz del proyecto en el que deberás ingresar:
> 	POSTGRES_USER= "nombre de usuario de postgres"

> 	POSTGRES_PASSWORD= "contraseña de postgres"

> 	POSTGRES_DB= "nombre de base de datos"

> 	POSTGRES_HOST= "ruta del host (por ejemplo localhost)"

#### Luego ejecutar el archivo main.py desde consola para descargar los archivos, leerlos, y guardarlos en la base de datos
> 	python3 main.py

#### Por último ejecutar scripts.py para procesar algunos datos y crear tablas extras
> 	python3 scripts.py
