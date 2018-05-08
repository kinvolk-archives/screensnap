#!/usr/bin/env python3

from urllib.parse import urlparse
import asyncio
import sys

from screensnap import screenshot


def main(args):
    url = 'https://kinvolk.io'
    if len(args) > 0:
        url = args[0]
    url_parts = urlparse(url)
    out_file = '{}.png'.format(url_parts.netloc)
    buf = asyncio.get_event_loop().run_until_complete(screenshot(url))
    with open(out_file, 'wb') as f:
        f.write(buf)


if __name__ == '__main__':
    main(sys.argv[1:])
