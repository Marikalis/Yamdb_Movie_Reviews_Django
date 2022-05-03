import csv
import os
import sqlite3

path = 'db.sqlite3'
con = sqlite3.connect(path)
cur = con.cursor()
script_dir = os.path.dirname(__file__)
with open(
    os.path.join(script_dir, 'static/data/users.csv'),
    'r',
    encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [(
        i['id'],
        i['username'],
        i['email'],
        i['role'],
        i['bio'],
        i['first_name'],
        i['last_name']) for i in dr]
cur.executemany("INSERT INTO reviews_user"
                "(id, username, email, role,"
                "bio, first_name, last_name, is_superuser,"
                "is_staff, is_active, date_joined)"
                "VALUES (?, ?, ?, ?, ?, ?, ?, false,"
                "false, false, false);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_user ", cur.rowcount)

with open(
        os.path.join(script_dir, 'static/data/category.csv'),
        'r',
        encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (i['id'],
         i['name'],
         i['slug']) for i in dr]
cur.executemany("INSERT INTO reviews_category"
                "(id, name, slug)"
                "VALUES (?, ?, ?);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_category ", cur.rowcount)

with open(
        os.path.join(script_dir, 'static/data/genre.csv'),
        'r',
        encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (i['id'],
         i['name'],
         i['slug']) for i in dr]
cur.executemany("INSERT INTO reviews_genre"
                "(id, name, slug)"
                "VALUES (?, ?, ?);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_genre ", cur.rowcount)

with open(
        os.path.join(script_dir, 'static/data/titles.csv'),
        'r',
        encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (i['id'],
         i['name'],
         i['year'],
         i['category']) for i in dr]
cur.executemany("INSERT INTO reviews_title"
                "(id, name, year, category_id)"
                "VALUES (?, ?, ?, ?);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_title ", cur.rowcount)

with open(
        os.path.join(script_dir, 'static/data/review.csv'),
        'r',
        encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (i['id'],
         i['title_id'],
         i['text'],
         i['author'],
         i['score'],
         i['pub_date']) for i in dr]
cur.executemany("INSERT INTO reviews_review"
                "(id, title_id, text, author_id, score, pub_date)"
                "VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_review ", cur.rowcount)

with open(
        os.path.join(script_dir, 'static/data/comments.csv'),
        'r',
        encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (i['id'],
         i['review_id'],
         i['text'],
         i['author'],
         i['pub_date']) for i in dr]
cur.executemany("INSERT INTO reviews_comment"
                "(id, review_id, text, author_id, pub_date)"
                "VALUES (?, ?, ?, ?, ?);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_comment ", cur.rowcount)

with open(
        os.path.join(script_dir, 'static/data/genre_title.csv'),
        'r',
        encoding='utf-8'
) as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (i['id'],
         i['title_id'],
         i['genre_id']) for i in dr]
cur.executemany("INSERT INTO reviews_title_genre"
                "(id, title_id, genre_id)"
                "VALUES (?, ?, ?);", to_db)
con.commit()
print("Запись успешно вставлена в таблицу reviews_title_genre ", cur.rowcount)

con.close()
