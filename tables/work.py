from connect import *


class Work:
    def __init__(self, post_id, description, deadline, number_of_room, hotel_id):
        self.post_id = post_id
        self.descr = description
        self.deadline = deadline
        self.room = number_of_room
        self.hotel_id = hotel_id
    def insert_into_bd(self):
        create_work = f"""
        INSERT INTO
        work (workID, postId, description, deadline, numberOfRoom, hotelId)
        VALUES
        (NULL, '{self.post_id}', '{self.descr}', '{self.deadline}','{self.room}', '{self.hotel_id}');
        """
        execute_query(connection, create_work)