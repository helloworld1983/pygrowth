#!/usr/bin/env python

"""
CLI for eventfile module
"""

import click
import pygrowth.common.eventfile
import pygrowth.common.counthistory


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


@cli.command(help="Dump header attributes of an event file")
@click.argument("file_path", type=click.Path(exists=True))
def show(file_path):
    eventfile = pygrowth.common.eventfile.open(file_path)
    click.echo(eventfile)


@cli.command(help="Extract count history or spectrum")
@click.argument("file_path", type=click.Path(exists=True))
def extract(file_path):
    eventfile = pygrowth.common.eventfile.open(file_path)
    extractor = pygrowth.common.counthistory.CountHistoryExtractor()
    options = {
        "time_axis": "absolute",
        "time_origin": 1514734663.0,
        "channel": 0,
        "energy_range_kev": [500, 3000],
        "duration_before_origin_sec": 30.0,
        "duration_after_origin_sec": 120.0,
    }
    counthistory = extractor.extract(eventfile, 10, options)
    click.echo(counthistory)
    for time_bin_center, time_bin_width, rate, rate_error in zip(
            counthistory.time_bin_center(), counthistory.time_bin_width(),
            counthistory.count_rate(), counthistory.count_rate_error()):
        click.echo([time_bin_center, time_bin_width, rate, rate_error])


def main():
    cli()


if __name__ == "__main__":
    main()