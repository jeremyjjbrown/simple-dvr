#!/usr/bin/python3

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import requests
import shutil


def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


def record():
    app.logger.info("Scheduler is alive!")


sched = BackgroundScheduler(daemon=True)
sched.add_job(record, 'interval', minutes=1)
sched.start()

app = Flask(__name__)


@app.route("/home")
def home():
    """ Function for test purposes. """
    return "Welcome Home :) !"


if __name__ == "__main__":
    app.run(port=8000)
