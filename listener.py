# -*- coding: utf-8 -*-
from core.core import Core
from flask import request
from api import sender
import logging
import click
import flask


app = flask.Flask(__name__)


@app.route('/pujar')
def default():
    logger = logging.getLogger('Flaskapp')
    logger.info('Pujant')


@app.route('/parar')
def default():
    logger = logging.getLogger('Flaskapp')
    logger.info('Parant')


@app.route('/baixar')
def default():
    logger = logging.getLogger('Flaskapp')
    logger.info('Baixant')


@click.command()
@click.option('-v', '--verbosity', is_flag=True, help='Show verbose output')
@click.option('-p', '--port', default=80, type=int, help='Port to listen on')
@click.option(
    '-i', '--interface', default='0.0.0.0', type=str, help='Interface to bind')
def startup(verbosity, port, interface):
    logging.basicConfig(
        format='[%(asctime)s][%(levelname)s]%(name)s: %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S',
        level=logging.INFO if verbosity else logging.WARNING
    )
    global house_core
    house_core = Core()
    if sender.getServerVersion() >= 400:
        exit(-1)
    # if sender.registerSubscriptions() >= 400:
    #     exit(-1)
    app.run(host=interface, port=port)


if __name__ == '__main__':
    startup()
