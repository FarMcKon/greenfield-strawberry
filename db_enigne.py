from sqlalchemy import create_engine
import os

def setup():
    ''' Only run once per new install'''
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    # cwd = os.getcwd()
    # file = "sw.sqlite"
    # full_path = f"sqlite://{cwd}/{file}
    # #engine = create_engine("sqlite://", echo=True)
    # engine = create_engine(full_path, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))