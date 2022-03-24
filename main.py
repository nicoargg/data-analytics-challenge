#Main functions
from get_data import download_csv
from read_csv import read_csv
#Sqlalchemy
from sqlalchemy import create_engine
import sqlalchemy
#pandas
import pandas as pd
#decouple
from decouple import config
import logging


LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logs/logs.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    encoding= "utf-8",
                    filemode = 'w')

logger = logging.getLogger()

def main(username:str, password:str, database_name:str, host:str):
    """With read_csv reads the data an saves in a postgresql database"
        
        Args:
            username (str): username to login in local server
            password (str): passqord to login in local server
            database_anme (str): name of the database you want to modify

        Returns: Nothing 
    """
    museo_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv"
    cine_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
    biblioteca_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"



    download_csv(biblioteca_url, "bibliotecas")
    logger.debug("# Datos de bibliotecas populares descargados")

    download_csv(cine_url, "cines")
    logger.debug("# Datos de salas de cine descargados")

    download_csv(museo_url, "museos")
    logger.debug("# Datos de museos descargados")

    # obtains two pandas tables
    data_biblioteca, not_normalized_biblioteca = read_csv("bibliotecas")
    logger.debug("# Bibliotecas.csv leído")
    data_cine, not_normalized_cine = read_csv("cines")
    logger.debug("# Cines.csv leído")
    data_museo, not_normalized_museo = read_csv("museos")
    logger.debug("# Museos.csv leído")    
    
    # It joins the three normalized tables
    all_data = pd.concat(([data_biblioteca,data_cine,data_museo]))

    # Conection to Database
    engine = create_engine(f'postgresql://{username}:{password}@{host}/{database_name}')

    c = engine.connect()
    logger.debug("# Conexión con base de datos exitosa")


    # Saving not normalized tables in database
    not_normalized_biblioteca.to_sql("bibliotecas", con = engine, if_exists='replace')
    logger.debug("# Tabla 'bibliotecas' en base de datos Creada")

    not_normalized_cine.to_sql("cines", con = engine, if_exists='replace')
    logger.debug("# Tabla 'cines' en base de datos Creada")

    not_normalized_museo.to_sql("museos", con = engine, if_exists='replace')
    logger.debug("# Tabla 'museos' en base de datos Creada")


    # Saving the normalized table in database
    all_data.to_sql("tabla_completa", con= engine, if_exists="replace")
    logger.debug("# Tabla con todos los datos Creada")
    
    c.close()

if __name__ == '__main__':
    main(config('POSTGRES_USER'), config('POSTGRES_PASSWORD'), config('POSTGRES_DB'), config('POSTGRES_HOST'))
    