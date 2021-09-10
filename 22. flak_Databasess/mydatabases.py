import mysql.connector


class Database:
    """
    this is used for communicating with MySQL DB
    """
    def __init__(self):
        self.__connection = mysql.connector.connect(
                host='localhost', user='root', password='root', database='personsdb')

    # used for execute the queries of type
    # - INSERT, UPDATE, DELETE
    def execute_query(self, query):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()

    # used for SELECT queries
    def select_query(self, query):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
