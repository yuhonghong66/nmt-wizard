import logging
import os
import sys

from six.moves import configparser

from nmtwizard import config, task
from nmtwizard.redis_database import RedisDatabase
from nmtwizard.worker import Worker

cfg = configparser.ConfigParser()
cfg.read('settings.ini')

logging.basicConfig(stream=sys.stdout, level=cfg.get('default', 'log_level'))
logger = logging.getLogger()

redis_password = None
if cfg.has_option('redis', 'password'):
    redis_password = cfg.get('redis', 'password')

redis = RedisDatabase(cfg.get('redis', 'host'),
                      cfg.getint('redis', 'port'),
                      cfg.get('redis', 'db'),
                      redis_password)

# make sure notify events are set
redis.config_set('notify-keyspace-events', 'Klgx')

services = config.load_services(cfg.get('default', 'config_dir'))

# remove busy state from resources
for key in redis.keys('busy:*'):
    redis.delete(key)
# remove reserved state from resources
for key in redis.keys('reserved:*'):
    redis.delete(key)

# On startup, add all active tasks in the work queue.
for task_id in task.list_active(redis):
    with redis.acquire_lock(task_id):
        status = redis.hget('task:'+task_id, 'status')
        if status == 'queue' or status == 'allocating':
            task.service_queue(redis, task_id, redis.hget('task:'+task_id, 'service'))
        else:
            task.work_queue(redis, task_id)

# TODO: start multiple workers here?
worker = Worker(redis, services,
                cfg.getint('default', 'refresh_counter'),
                cfg.getint('default', 'quarantine_time'))
worker.run()
