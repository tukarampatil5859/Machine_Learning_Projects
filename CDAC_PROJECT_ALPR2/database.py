import mysql.connector


class Database:
    def __init__(self):
        self.__connection = mysql.connector.connect(
            host="localhost",user="root",password="Sunbeam@123",database="car"
        )

    def query(self, query):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()
        cursor.close()

    def select(self, query):
        cursor = self.__connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data

    def __del__(self):
        self.__connection.close()
