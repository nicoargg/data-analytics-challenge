import csv


def read_csv(file: str, category: str):
    """Reads csv file with the path: "data/{category}/hola/{category}"
        
        Args:
            file (str): name of the csv file you want to read
            category (str): name of the category of the file

        Returns: Nothing 
    """
    folder = f"data/{category}/hola/{category}"
    f = open(f"{folder}/{file}", encoding="utf-8")
    reader = csv.reader(f)

    
    # Appends first line of csv
    data = []

    cod_localidad = "cod_localidad"
    id_provincia = "id_provincia"
    id_departamento = "id_departamento"
    categoria = "categoria"
    provincia = "provincia"
    localidad = "localidad"
    nombre = "nombre"
    domicilio = "domicilio"
    codigo_postal = "codigo_postal"
    num_telefono = "num_telefono"
    mail = "mail"
    web = "web"

    header_list = [cod_localidad,id_provincia,id_departamento,
                    categoria, provincia, localidad, nombre, domicilio,
                    codigo_postal, num_telefono, mail, web]
    
    data.append(header_list) # First line

    header = next(reader)  #jump first line of reader

    print(data)
    for row in reader:
        # Row = [cod_localidad, id_provincia, id_departamento, categoria, provincia, localidad, nombre, domicilio, codigo_postal, num_telefono, mail, web]
        cod_localidad = str(row[0])
        id_provincia = int(row[1])
        id_departamento = int(row[2])
        categoria = str(row[4])
        provincia = str(row[6])
        localidad = str(row[7])
        nombre = str(row[8])
        domicilio = str(row[9])
        codigo_postal = str(row[11])
        num_telefono = str(row[13])
        mail = str(row[14])
        web = str(row[15])

        data.append([cod_localidad, id_provincia, id_departamento,
                     categoria, provincia, localidad, nombre, 
                     domicilio, codigo_postal, num_telefono,
                     mail, web])

    print(data)

