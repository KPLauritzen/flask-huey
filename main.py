from flask import Flask, url_for, redirect
from tasks import do_async_task
from config import huey

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/task")
def task_route():
    res = do_async_task()
    return redirect(url_for("status", task_id=res.id))


@app.route("/status/<task_id>")
def status(task_id):
    res = huey.result(task_id)
    if res is None:
        return "Task is queued"
    else:
        return res


if __name__ == '__main__':
    app.run(port=5000)
