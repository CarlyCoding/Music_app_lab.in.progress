# import code goes here when I get to it. 

from flask import after_this_request

from code.models.artist import Artist


def save(artist):
    # This line is the SQL code- for what we are doing eg. adding an artist
    # to a database. The code is generalised eg. %s 
    sql = "INSERT INTO artists (name) VALUE (%s) RETURNING *"
    # The value is the artists name. 
    values = [artist.name]
    # Using a variable so we can attach the results
    results = run_sql(sql, values)
    # Giving the results an id that will generate itself 
    id = results[0]['id']
    # artist id will be assigned the id
    artist.id = id
    # return actually makes this do something after the function runs. 
    return artist

# To be used for deleting all the artists- just deletes all from artists. 
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    # Empty variable for artist as we will be selecting
    artist = None
    # sql code for selecting from the database
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'] )
    return artist







