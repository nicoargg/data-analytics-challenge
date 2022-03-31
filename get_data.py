import os

import requests

import datetime


def download_csv(url:str, category:str):
    """Downloads a file and saves it as .csv with 
    the next path: 
        "./{category}/{this year}-{this month}/{category}-{date}.csv"
    
    Args:
        url (str): url of the file you want to download
        category (str): name of category you want
    
    Returns: Nothing
    """

    months = ("enero", "febrero", "marzo", "abri", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    months = months[datetime.date.today().month - 1]
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    folder = f"{category}/{datetime.date.today().year}-{months}"

    # If folder's path doesn't exist, it is created
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        req = requests.get(url, auth=("user", "pass"))
        if req.status_code == 200:
            content = req.content
        else:
            raise ValueError(f'Error: {req.status_code}')
    except ValueError as ve:
        print(ve)
    try:
        f = open(f"{folder}/{category}-{date}.csv", "wb+")
        f.write(content)
    finally:
        f.close()