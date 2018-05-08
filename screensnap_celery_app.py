# vi: set ft=python :

import asyncio
import os

from celery import Celery
from dotenv import load_dotenv
from screensnap import screenshot
from screensnap_storage import put

load_dotenv(verbose=True)

app = Celery('screensnap', broker=os.getenv('SCREENSNAP_REDIS_URL',
                                            'redis://localhost:6379/0'))


@app.task
def screenshot_task(url, screenshot_id):
    buf = asyncio.get_event_loop().run_until_complete(screenshot(url))
    put('{}.png'.format(screenshot_id), buf)
