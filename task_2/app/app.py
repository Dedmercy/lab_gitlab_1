import requests
import os
import json

server = os.environ['SERVER']
port = os.environ['PORT']


def get_worst_student_info():

    response = requests.get(f'http://{server}:{port}/get-worst-student-info/')

    print(response.status_code, response.json())

    with open('result/result.txt', 'w') as file:
        file.write(json.dumps(response.json()))

    print('Ответ получен !!!')


if __name__ == '__main__':
    get_worst_student_info()