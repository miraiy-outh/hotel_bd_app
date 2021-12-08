user_dict = {
    'operator': [['operator1', '1234'], ['operator2', '1234']],
    'admin': [['admin1', '1234'], ['admin2', '1234']]
}


def add_to_dict(login, password, role):
    user_dict[role] = (login, password)