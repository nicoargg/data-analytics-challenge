import pandas as pd


def read_csv(file: str, category: str):
    """Reads csv file with the path: "data/{category}/hola/{category}"
        
        Args:
            file (str): name of the csv file you want to read
            category (str): name of the category of the file

        Returns: Nothing 
    """
    folder = f"data/{category}/hola/{category}"
    reader = pd.read_csv(f'{folder}/{file}')

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

