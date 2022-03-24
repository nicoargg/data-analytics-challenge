from sqlalchemy import create_engine
from decouple import config

engine = create_engine(f'postgresql://{config("POSTGRES_USER")}:{config("POSTGRES_PASSWORD")}@{config("POSTGRES_HOST")}/{config("POSTGRES_DB")}')

try:
    c = engine.connect()
    engine.execute(open("sql/registrostotales.sql", "r").read())
    engine.execute(open("sql/porprovincia.sql", "r").read())
    engine.execute(open("sql/cinesprocesado.sql", "r").read())
finally:
    c.close()