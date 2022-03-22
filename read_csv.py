#pandas
import pandas as pd
#datetime
import datetime

def read_csv(category: str):
    """Reads csv file with the path: "data/{category}/hola/{category}"
        
        Args:
            category (str): name of the category of the file

        Returns: a pandas table
    """
    months = ("enero", "febrero", "marzo", "abri", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    months = months[datetime.date.today().month - 1]
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    folder = f"{category}/{datetime.date.today().year}-{months}"
    reader = pd.read_csv(f'{folder}/{category}-{date}.csv')

    rename_columns = {
        'Cod_Loc': 'cod_localidad',
    'IdProvincia': 'id_provincia',
    'IdDepartamento':'id_departamento',
    'cod_loc': 'cod_localidad',
    'idprovincia': 'id_provincia',
    'iddepartamento':'id_departamento',
    'Categoría':'categoria',
    'Provincia':'provincia',
    'Localidad':'localidad',
    'Nombre':'nombre',
    'Domicilio':'domicilio',
    'Dirección':'domicilio',
    'direccion':'domicilio',
    'CP':'codigo_postal',
    'Teléfono':'num_telefono',
    'telefono':'num_telefono',
    'Mail':'mail',
    'Web':'web'
    }

    reader.rename(columns=rename_columns, inplace=True)


    columns = ["cod_localidad", 
    "id_provincia", 
    "id_departamento", 
    "categoria", 
    "provincia", 
    "localidad", 
    "nombre", 
    "domicilio", 
    "codigo_postal", 
    "num_telefono",
    "mail", 
    "web"]

    return(reader[columns])

