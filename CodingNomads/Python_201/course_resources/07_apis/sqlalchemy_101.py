# py -m pip install sqlalchemy
# py -m pip install pymysql
# py -m pip install cryptography
import sqlalchemy as sql
from pathlib import Path

def getDBlogin():
    txt = Path().resolve().joinpath('CodingNomads/Python_201/course_resources/07_apis/secrets.txt')

    with txt.open('r') as Input:
        text = Input.read()
        secrets = {l.split('=')[0]: l.split('=')[1] for  l in text.split('\n')}
    return secrets

def getDBstring(login_details):
    return f"mysql+pymysql://{login_details['username']}:{login_details['password']}@localhost/sakila"

eng = sql.create_engine(getDBstring(getDBlogin()))

con = eng.connect()
metadata = sql.MetaData()

actor = sql.Table('actor', metadata, autoload_with=eng)
film = sql.Table('film', metadata, autoload_with=eng)
# actor = sql.Table('actor', metadata, autoload=True, autoload_with=eng)

actor.columns.keys()
repr(metadata.tables['actor'])

# query actor table ----

# 1) SELECT * FROM actor
query = sql.select(actor) 
res = con.execute(query)

out = res.fetchmany(5)

# 2) SELECT * FROM actor WHERE first_name = "PENELOPE";
q2 = sql.select(actor).where(actor.columns.first_name == 'PENELOPE')

res2 = con.execute(q2)
res2.fetchall()

# 3) IN
q3 = sql.select(actor).where(actor.columns.first_name.in_(['PENELOPE', 'JOHN', 'UMA']))

res3 = con.execute(q3)
res3.fetchall()

# 4) AND, OR, NOT
q4 = sql.select(film).where(sql.and_(film.columns.length > 60, film.columns.rating == 'PG'))
q5 = sql.select(film).where(sql.and_(film.columns.length > 60, film.columns.rating != 'PG'))

orderby = sql.select(film).order_by(sql.asc(film.columns.replacement_cost))

res3 = con.execute(orderby)
res3.fetchmany(5)

film.columns.keys()

# 5) SUM + other f(x)s
sumqry = sql.select(sql.func.sum(film.columns.length))

res4 = con.execute(sumqry)
res4.fetchall()