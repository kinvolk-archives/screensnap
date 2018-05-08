# screensnap

screensnap is a small Python demo web service to create screenshots.

Please note: it's built for training purposes only, contains various
shortcuts and should **not** be used outside of a demo environment.

## Local setup

Install chromium:

```
sudo apt-get update && sudo apt-get install -y chromium-browser
```

Setup the Python virtual env:

```
cd screensnap
python3 -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
```

Start the redis server:

```
docker run --rm --name redis -p 6379:6379 redis:alpine
```

Start the minio server:

```
docker run -p 9000:9000 minio/minio server /data
```

Create a `.env` file with minimal configuration. The Minio access and
secret key can be found in the CLI output of the Minio Docker container.

Example `.env`:

```
SCREENSNAP_S3_ENDPOINT=http://localhost:9000
SCREENSNAP_S3_ACCESS_KEY=YGJ...
SCREENSNAP_S3_SECRET_KEY=59P...
```

Start the celery worker:

```
source venv/bin/activate
celery -A screensnap_celery_app worker --loglevel=info
```

Start the screensnap server:

```
source venv/bin/activate
./server.py
```

Go to http://localhost:5000

## Other commands

Get a redis command line:

```
docker run --rm -it --link redis redis:alpine redis-cli -h redis -p 6379
```
