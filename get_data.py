import os

from urllib.request import Request, urlopen




def download_csv(url:str, file:str, category:str):
    """Downloads a file and saves it with the name you want
    in the next path: data/{category}/{}/{file}
    
    Args:
        url (str): url of the file you want to download
        file (str): name of the file you want to save
        category (str): name of category you want
    
    Returns: Nothing
    """
    folder = f"data/{category}/hola/{category}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    f = open(f"{folder}/{file}", "wb+")
    f.write(webpage)
    f.close


museo_url = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv"