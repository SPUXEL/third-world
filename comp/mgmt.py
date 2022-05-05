import sqlite3, json


with sqlite3.connect('database.db') as database:
    cursor = database.cursor()


class MGMT:
    def __init__(self, user_id):
        self.user_id = user_id


    def add_user(self, user):
        data_dict = {
                'user': {
                    'username': user.first_name
                    },
                'cache': {
                    },
                'statistics': {
                    }
                }

        data_json = json.dumps(data_dict)

        cursor.execute(
            '''
            INSERT INTO users (user_id, user_data)
            VALUES (?, ?)
            ''', (self.user_id, data_json)
            )

        database.commit()


    def get_user(self):
        cursor.execute(
            f'SELECT user_data FROM users WHERE user_id = {self.user_id}'
            )
        data_tuple = cursor.fetchone()

        if data_tuple == None:
            return None
        else:
            data_str = data_tuple[0]
            data_dict = json.loads(data_str)

            return data_dict


    def save(self):
        pass

