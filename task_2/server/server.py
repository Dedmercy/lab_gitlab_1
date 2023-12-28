import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/get-worst-student-info/')
async def get_worst_student_info():

    with open('data.json', 'r') as file:
        data = file.read()

    students = json.loads(data)

    worst_sum = 15
    result = {}

    for student in students:

        grades_sum = sum(student['grades'].values())

        if grades_sum <= worst_sum:
            result = student
            worst_sum = grades_sum

    return result


if __name__ == '__main__':
    uvicorn.run(app, host='server', port=8080)
