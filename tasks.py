from config import huey
from time import sleep


@huey.task()
def do_async_task():
    sleep(5)
    return "lol, you waited all this time for this?"
