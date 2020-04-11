from OnlineGameHall.celery import app
from django.http import HttpResponse
import time



@app.task
def task_test(file_path,myfile):
    with open(file_path, 'wb') as f:
        data = myfile.file.read()
        f.write(data)
    return HttpResponse("OK")