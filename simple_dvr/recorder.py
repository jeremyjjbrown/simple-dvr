#!/usr/bin/env python3


import eventlet
import requests
import shutil
import click

from datetime import datetime


def record(url, local_filename, duration):
    with eventlet.Timeout(duration):
        with requests.get(url, stream=True, timeout=10, verify=False) as r:
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)


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

    record(url, f"{name}.mpeg", int(duration))


if __name__ == "__main__":
    cli()
