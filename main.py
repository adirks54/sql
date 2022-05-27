import sqlalchemy
import pprint



engine = sqlalchemy.create_engine('postgresql://postgres:password@localhost:5432/postgres')
engine


connection = engine.connect()

connection.execute("INSERT INTO singer VALUES ( 1,'Би-2');")
connection.execute("INSERT INTO singer VALUES ( 2,'Сплин');")
connection.execute("INSERT INTO singer VALUES ( 3,'Тату');")
connection.execute("INSERT INTO singer VALUES ( 4,'Круг');")
connection.execute("INSERT INTO singer VALUES ( 5,'Киркоров');")
connection.execute("INSERT INTO singer VALUES ( 6,'Любе');")
connection.execute("INSERT INTO singer VALUES ( 7,'U2');")
connection.execute("INSERT INTO singer VALUES ( 8,'Кабзон');")

connection.execute("INSERT INTO gengre VALUES (1, 'Рок');")
connection.execute("INSERT INTO gengre VALUES (2, 'Рэп');")
connection.execute("INSERT INTO gengre VALUES (3, 'Поп');")
connection.execute("INSERT INTO gengre VALUES (4, 'Шансон');")
connection.execute("INSERT INTO gengre VALUES (5, 'Классика');")


connection.execute("INSERT INTO album VALUES (1, 'Серебро', '2005');")
connection.execute("INSERT INTO album VALUES (2, 'Колхоз', '2001');")
connection.execute("INSERT INTO album VALUES (3, 'Bono', '2011');")
connection.execute("INSERT INTO album VALUES (4, 'TATU', '2011');")
connection.execute("INSERT INTO album VALUES (5, 'Я', '2009');")
connection.execute("INSERT INTO album VALUES (6, 'Выхода нет', '2014');")
connection.execute("INSERT INTO album VALUES (7, 'Роза', '1998');")
connection.execute("INSERT INTO album VALUES (8, 'Ангел', '1999');")


connection.execute("INSERT INTO track VALUES (1, 'Полковнику никто не пишет', '03:12', 1);")
connection.execute("INSERT INTO track VALUES (2, 'Выхода нет', '03:14', 6);")
connection.execute("INSERT INTO track VALUES (3, 'Выходи', '5:12', 7);")
connection.execute("INSERT INTO track VALUES (4, 'Как дела', '04:11', 2);")
connection.execute("INSERT INTO track VALUES (5, 'Остаемся зимовать', '05:16', 6);")
connection.execute("INSERT INTO track VALUES (6, 'Я и ты', '02:12', 4);")
connection.execute("INSERT INTO track VALUES (7, 'Привет', '03:22', 8);")
connection.execute("INSERT INTO track VALUES (8, 'Как', '03:15', 5);")
connection.execute("INSERT INTO track VALUES (9, 'Никак', '03:52', 5);")
connection.execute("INSERT INTO track VALUES (10, 'Сколько', '03:18', 2);")
connection.execute("INSERT INTO track VALUES (11, 'Можно', '03:52', 6);")
connection.execute("INSERT INTO track VALUES (12, 'T1', '05:12', 3);")
connection.execute("INSERT INTO track VALUES (13, 'Ну', '02:12', 8);")
connection.execute("INSERT INTO track VALUES (14, 'Ну-да', '04:12', 1);")
connection.execute("INSERT INTO track VALUES (15, 'Пока', '03:12', 5);")


connection.execute("INSERT INTO sbor VALUES (1, 'Пляски', '2019');")
connection.execute("INSERT INTO sbor VALUES (2, 'Руки', '2021');")
connection.execute("INSERT INTO sbor VALUES (3, 'Привет', '2009');")
connection.execute("INSERT INTO sbor VALUES (4, 'Пока', '2019');")
connection.execute("INSERT INTO sbor VALUES (5, 'День', '2017');")
connection.execute("INSERT INTO sbor VALUES (6, 'Ночь', '2019');")
connection.execute("INSERT INTO sbor VALUES (7, 'Тьма', '2019');")
connection.execute("INSERT INTO sbor VALUES (8, 'Огонь', '2012');")

connection.execute("INSERT INTO gengre_sing VALUES (1, 1, 1);")
connection.execute("INSERT INTO gengre_sing VALUES (2, 1, 2);")
connection.execute("INSERT INTO gengre_sing VALUES (3, 1, 7);")
connection.execute("INSERT INTO gengre_sing VALUES (4, 3, 3);")
connection.execute("INSERT INTO gengre_sing VALUES (5, 3, 5);")
connection.execute("INSERT INTO gengre_sing VALUES (6, 4, 4);")
connection.execute("INSERT INTO gengre_sing VALUES (7, 5, 6);")
connection.execute("INSERT INTO gengre_sing VALUES (8, 5, 8);")

connection.execute("INSERT INTO album_isp VALUES (1, 1, 1);")
connection.execute("INSERT INTO album_isp VALUES (2, 2, 5);")
connection.execute("INSERT INTO album_isp VALUES (3, 3, 7);")
connection.execute("INSERT INTO album_isp VALUES (4, 4, 3);")
connection.execute("INSERT INTO album_isp VALUES (5, 5, 6);")
connection.execute("INSERT INTO album_isp VALUES (6, 6, 2);")
connection.execute("INSERT INTO album_isp VALUES (7, 7, 4);")
connection.execute("INSERT INTO album_isp VALUES (8, 8, 8);")


connection.execute("INSERT INTO sbor_tr VALUES (1, 1, 1);")
connection.execute("INSERT INTO sbor_tr VALUES (2, 2, 4);")
connection.execute("INSERT INTO sbor_tr VALUES (3, 4, 6);")
connection.execute("INSERT INTO sbor_tr VALUES (4, 5, 7);")
connection.execute("INSERT INTO sbor_tr VALUES (5, 6, 4);")
connection.execute("INSERT INTO sbor_tr VALUES (6, 2, 3);")
connection.execute("INSERT INTO sbor_tr VALUES (7, 2, 5);")
connection.execute("INSERT INTO sbor_tr VALUES (8, 3, 1);")
connection.execute("INSERT INTO sbor_tr VALUES (9, 3, 4);")
connection.execute("INSERT INTO sbor_tr VALUES (10, 11, 7);")
connection.execute("INSERT INTO sbor_tr VALUES (11, 12, 4);")
connection.execute("INSERT INTO sbor_tr VALUES (12, 12, 5);")
connection.execute("INSERT INTO sbor_tr VALUES (13, 13, 3);")
connection.execute("INSERT INTO sbor_tr VALUES (14, 14, 4);")
connection.execute("INSERT INTO sbor_tr VALUES (15, 15, 6);")


#
#


print(connection.execute("SELECT * FROM sbor_tr;").fetchall())