# Import Python packages
import os
import glob
import csv
from queries import res

def create_list_of_file_paths():
    # checking your current working directory
    print(os.getcwd())

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root, '*'))
        print(file_path_list)
    return file_path_list

def create_csv(file_path_list):
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = []

    # for every filepath in the file path list
    for f in file_path_list:
        # reading csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader)

            # extracting each data row one by one and append it
            for line in csvreader:
                # print(line)
                full_data_rows_list.append(line)

    # uncomment the code below if you would like to get total number of rows
    print(len(full_data_rows_list))
    # uncomment the code below if you would like to check to see what the list of event data rows will look like
    #print(full_data_rows_list)

    # delete file if it already exists
    filename='event_datafile_new.csv'
    try:
        os.remove(filename)
    except OSError:
        pass

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length',
                         'level', 'location', 'sessionId', 'song', 'userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
    return filename

def process_data(file, query, columns, session):

    with open(file, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            session.execute(query, ( line[column] for column in columns ))



def main():
    file=create_csv(create_list_of_file_paths())

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

    for query in res:
        process_data(file, query, res[query], session)











if __name__ == "__main__":
    main()





