# Flask app with Huey for background tasks
Stealing an idea from Dingobars nice [Celery + FastAPI](https://github.com/dingobar/fast-api-celery) example, 
and tearing out both Celery and FastAPI.

## Quick start
Make a virtualenv and activate it. Then
`pip install -r requirements.txt`. 

Now start the Huey task consumer with 
`huey_consumer.py main.huey` if you are on linux and
`huey_consumer.exe main.huey` on windows. Make sure you are in the project root. 

Now start the Flask server: `python main.py`. 

Go to `localhost:5000/task` and see that you are redirected to a status page. 
Refreshing this page will eventually get you the result of the task. 