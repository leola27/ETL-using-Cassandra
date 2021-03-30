import cassandra
from queries import create_table_queries, drop_table_queries


def create_database():
    # This should make a connection to a Cassandra instance your local machine
    # (127.0.0.1)
    from cassandra.cluster import Cluster
    cluster = Cluster()

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()

    # TO-DO: Create a Keyspace
    try:
        session.execute("""
        CREATE KEYSPACE IF NOT EXISTS udacityodenisova
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
                        )

    except Exception as e:
        print(e)



    # TO-DO: Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('udacityodenisova')
    except Exception as e:
        print(e)

    except Exception as e:
        print(e)
    return session,cluster


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)


def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)


def main():
    """
    - Drops (if exists) and Creates the  database.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.
    """
    session, cluster=create_database()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()