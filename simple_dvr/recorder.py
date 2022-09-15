#!/usr/bin/env python3


import click
import eventlet
import ffmpeg
import psutil
import requests
import shutil
import time

from datetime import datetime


def record(url, local_filename, duration):
    with eventlet.Timeout(duration):
        try:
            with requests.get(url, stream=True, timeout=10, verify=False) as r:
                with open(f"{local_filename}.mpeg", 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
        except Exception as e:
            print(e)


def record_mkv(url, local_filename, duration):
    process = ffmpeg.input(url).output(f"{local_filename}.mkv")\
        .overwrite_output().run_async()
    time.sleep(duration)
    pid = psutil.Process(process.pid)
    for proc in pid.children(recursive=True):
        proc.kill()
    pid.kill()


@click.command()
@click.option('-c', '--channel')
@click.option('-d', '--duration')
@click.option('-n', '--name')
@click.option(
    '-s', '--start',
    type=click.DateTime(formats=["%Y-%m-%dT%H:%M:%S", "%m-%dT%H:%M"]),
    default=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
)
def cli(channel, duration, name, start):
    if start.year == 1900:
        start = start.replace(datetime.now().year)
    start_time = start.strftime("%Y-%m-%dT%H:%M:%S")

    click.echo(f'recording {channel} on {start_time}' +
               f' for {duration} seconds to {name}.mpeg')
    url = f'http://192.168.1.38:5004/auto/v{channel}?' + \
        'transcode=internet540&duration={duration}'

    record_mkv(url, name, int(duration))


if __name__ == "__main__":
    cli()
