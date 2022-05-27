import sqlalchemy
import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:password@localhost:5432/postgres')
engine
connection = engine.connect()


select_1 = connection.execute("SELECT name, album_date FROM album "
                        "WHERE album_date=2005;").fetchall()

select_2 = connection.execute("SELECT name,lenth FROM track "
                        "WHERE lenth=(SELECT MAX(lenth) FROM track);").fetchall()

select_3 = connection.execute("SELECT name,lenth FROM track "
                        "WHERE lenth>='03:30';").fetchall()

select_4 = connection.execute("SELECT name,sbor_date FROM sbor "
                        "WHERE  sbor_date BETWEEN 2018 AND 2020;").fetchall()

select_5 = connection.execute("SELECT name FROM singer "
                        "WHERE name NOT LIKE '%% %%' ;").fetchall()

select_6 = connection.execute("SELECT name FROM track "
                              "WHERE name LIKE '%%Вых%%';").fetchall()



print(select_6)


