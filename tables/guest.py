from connect import *


class Guest:
    def __init__(self, id, card_info, room, bill, a_time, d_time):
        self.id = id
        self.card_info = card_info
        self.room = room
        self.bill = bill
        self.a_time = a_time
        self.d_time = d_time

    def insert_into_bd(self):
        create_guest = f"""
        INSERT INTO
        guest (clientId, cardInformation, numberOfRoom, bill, arrivalTime, departureTime)
        VALUES
        ('{self.id}','{self.card_info}','{self.room}','{self.bill}','{self.a_time}','{self.d_time}');
        """
        execute_query(connection, create_guest)