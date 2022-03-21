#Main functions
from get_data import download_csv
from read_csv import read_csv
#Sqlalchemy
from sqlalchemy import create_engine
#pandas
import pandas as pd




def main(username, password, database_name):
    museo_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv"
    cine_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
    biblioteca_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"



    download_csv(biblioteca_url, "biblioteca.csv", "biblioteca")
    download_csv(cine_url, "cine.csv", "cine")
    download_csv(museo_url, "museo.csv", "museo")

    data_biblioteca = read_csv("biblioteca.csv", "biblioteca")
    data_cine = read_csv("cine.csv", "cine")
    data_museo = read_csv("museo.csv", "museo")
    

    engine = create_engine(f'postgresql://{username}:{password}@localhost/{database_name}')

    data_biblioteca.to_sql("biblioteca", con = engine, if_exists='replace')
    data_cine.to_sql("cine", con = engine, if_exists='replace')
    data_museo.to_sql("museo", con = engine, if_exists='replace')



if __name__ == '__main__':
    main()
