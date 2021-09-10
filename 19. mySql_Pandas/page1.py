import mysql.connector


def select_records():
    # connect to the database
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='personsdb')

    # create the query
    query = "select id, name, address, age, email from person"

    # get the cursor (in-memory table)
    cursor = connection.cursor()

    # execute the query
    cursor.execute(query)

    # get the query result
    result = cursor.fetchall()

    # process the result
    # print(result)
    # for row in result:
    #     print(f"id = {row[0]}")
    #     print(f"name = {row[1]}")
    #     print(f"address = {row[2]}")
    #     print(f"age = {row[3]}")
    #     print(f"email = {row[4]}")
    #     print("-" * 80)

    for (id, name, address, age, email) in result:
        print(f"id = {id}")
        print(f"name = {name}")
        print(f"address = {address}")
        print(f"age = {age}")
        print(f"email = {email}")
        print("-" * 80)

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()


def insert_record():
    print(f"enter name: ")
    name = input()

    print(f"enter address: ")
    address = input()

    print(f"enter age: ")
    age = input()

    print(f"enter email: ")
    email = input()

    # open the connection
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='personsdb')

    # create the query
    query = f"insert into person (name, address, age, email) values ('{name}', '{address}', '{age}', '{email}')"

    # get the cursor
    cursor = connection.cursor()

    # execute the query
    cursor.execute(query)

    # commit the changes to the db
    connection.commit()

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()


def update_record():
    # open the connection
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='personsdb')

    # create query
    query = f"update person set name = 'bill gates', address = 'usa' where id = 5"

    # get the cursor
    cursor = connection.cursor()

    # execute query
    cursor.execute(query)

    # commit the changes
    connection.commit()

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()


def delete_record():
    # open connection
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='personsdb')

    # create the query
    query = f"delete from person where id = 3"

    # get the cursor
    cursor = connection.cursor()

    # execute the query
    cursor.execute(query)

    # commit the changes
    connection.commit()

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()


# insert_record()
select_records()
# update_record()
# delete_record()
