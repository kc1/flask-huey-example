# config.py
from huey import RedisHuey
import os

basedir = os.path.abspath(os.path.dirname(__file__))
FLASK_CONFIG = os.getenv('FLASK_CONFIG')


if FLASK_CONFIG and FLASK_CONFIG == "production":

    REDIS_URL = os.getenv('REDISTOGO_URL')
    huey = RedisHuey('my-queue', url=REDIS_URL)
else:
    huey = RedisHuey()
