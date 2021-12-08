from connect import *


class Employee:
    def __init__(self, post, hotel, work_days, salary, name, phone_number):
        self.post = post
        self.hotel = hotel
        self.wd = work_days
        self.salary = salary
        self.name = name
        self.number = phone_number

    def insert_into_bd(self):
        create_employee = f"""
        INSERT INTO
        employee (employeeId, postId, hotelId, workDays, salary, fullName, phoneNumber)
        VALUES
        (NULL,'{self.post}','{self.hotel}','{self.wd}','{self.salary}','{self.name}','{self.number}');
        """
        execute_query(connection, create_employee)