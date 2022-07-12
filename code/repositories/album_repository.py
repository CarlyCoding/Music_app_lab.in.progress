# import code goes here when I get to it. 


def save(album):
    # Same format as the artist function with more stuff in it
    sql = "INSERT INTO albums (name, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album




