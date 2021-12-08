from connect import *


class Client:
    def __init__(self, full_name, passport, phone_number):
        self.full_name = full_name
        self.passport = passport
        self.phone_number = phone_number

    def insert_into_bd(self):
        create_client = f"""
        INSERT INTO
        client (clientId, fullName, passportInformation, phoneNumber)
        VALUES
        (NULL, '{self.full_name}','{self.passport}', '{self.phone_number}');
        """
        execute_query(connection, create_client)

