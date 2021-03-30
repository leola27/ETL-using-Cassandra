# DROP TABLES
drop_query1 = "drop table if exists sessionid_and_item_in_session"
drop_query2 = "drop table if exists user_id_session_id"
drop_query3 = "drop table if exists all_hands_against_his_own"

# CREATE TABLES
## Query 1:  Give me the artist, song title and song's length in the music app history that was heard during \
## sessionId = 338, and itemInSession = 4
create_query1 = "CREATE TABLE IF NOT EXISTS  sessionid_and_item_in_session "
create_query1 = create_query1 + "(artist_name text, song_title text, song_length text, session_id text, item_in_session text, PRIMARY KEY (session_id, item_in_session))"

## Query 2: Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name)\
## for userid = 10, sessionid = 182
create_query2 = "CREATE TABLE IF NOT EXISTS  user_id_session_id "
create_query2 = create_query2 + "(artist_name text, song_title text, first_name text, last_name text, user_id text, session_id text,item_in_session text, PRIMARY KEY (user_id, session_id, item_in_session))"

##  Query 3: Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
create_query3 = "CREATE TABLE IF NOT EXISTS  all_hands_against_his_own "
create_query3 = create_query3 + "(first_name text, last_name text, song_title text, PRIMARY KEY (song_title,first_name))"



#INSERT QUERIES
insert_query1 = "INSERT INTO sessionid_and_item_in_session (artist_name, song_title, song_length, session_id, item_in_session)"
insert_query1 = insert_query1 + "VALUES (%s, %s, %s, %s,%s)"
columns1=[0,9,5,8,3]

insert_query2 = "INSERT INTO user_id_session_id (artist_name, song_title, first_name, last_name, user_id,session_id,item_in_session)"
insert_query2 = insert_query2 + "VALUES (%s, %s, %s, %s,%s,%s,%s)"
columns2=[0,9,1,4,10,8,3]

insert_query3 = "INSERT INTO all_hands_against_his_own (first_name, last_name, song_title)"
insert_query3 = insert_query3 + "VALUES (%s, %s, %s)"
columns3=[1,4,9]

# QUERY LISTS
create_table_queries = [create_query1 , create_query2, create_query3]
drop_table_queries = [drop_query1, drop_query2, drop_query3]
insert_queries = [insert_query1 , insert_query2, insert_query3]
column_lists=[columns1,columns2,columns3]
res = {insert_queries[i]: column_lists[i] for i in range(len(insert_queries))}