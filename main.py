#Main functions
from get_data import download_csv
from read_csv import read_csv
#Sqlalchemy
from sqlalchemy import create_engine
#pandas
import pandas as pd




def main(username, password, database_name):
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
    download_csv(cine_url, "cines")
    download_csv(museo_url, "museos")
    print("end downloads")

    data_biblioteca = read_csv("bibliotecas")
    data_cine = read_csv("cines")
    data_museo = read_csv("museos")
    print("end readings")
    
    all_data = pd.concat(([data_biblioteca,data_cine,data_museo]))

    engine = create_engine(f'postgresql://{username}:{password}@localhost/{database_name}')

    data_biblioteca.to_sql("biblioteca", con = engine, if_exists='replace')
    data_cine.to_sql("cine", con = engine, if_exists='replace')
    data_museo.to_sql("museo", con = engine, if_exists='replace')

    all_data.to_sql("Tabla completa", con= engine, if_exists="replace")
    print("added to database")

if __name__ == '__main__':
    main("#username", "#password", "#database_name")
    