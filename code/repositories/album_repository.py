# import code goes here when I get to it. 


from optparse import Values
from unittest import result

from code.repositories import artist_repository

from code.models.album import Album


def save(album):
    # Same format as the artist function with more stuff in it
    sql = "INSERT INTO albums (name, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

# Delete for all the albums
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['name'], result['genre'], result['artist'], result['id'])
    return album


