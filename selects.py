# This should make a connection to a Cassandra instance your local machine
# (127.0.0.1)

from cassandra.cluster import Cluster
cluster = Cluster()

# To establish connection and begin executing queries, need a session
session = cluster.connect()


# TO-DO: Set KEYSPACE to the keyspace specified above
try:
    session.set_keyspace('udacityodenisova')
except Exception as e:
    print(e)

## TO-DO: Add in the SELECT statement to verify the data was entered into the table
query = "select artist_name, song_title, song_length from sessionid_and_item_in_session where session_id = '338' and item_in_session = '4'"
try:
    rows=session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print(row.artist_name, row.song_title, row.song_length)


## TO-DO: Add in the SELECT statement to verify the data was entered into the table
query = "select artist_name, song_title, first_name,last_name from user_id_session_id where user_id = '10' and session_id = '182'"
try:
    rows=session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print(row.artist_name, row.song_title, row.first_name, row.last_name)

## TO-DO: Add in the SELECT statement to verify the data was entered into the table
query = "select first_name,last_name from all_hands_against_his_own where song_title='All Hands Against His Own'"
try:
    rows=session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print(row.first_name, row.last_name)