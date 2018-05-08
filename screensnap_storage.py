# vi: set ft=python :

import os

from dotenv import load_dotenv
import boto3

load_dotenv(verbose=True)

_s3_client = boto3.client(
    's3',
    endpoint_url=os.getenv('SCREENSNAP_S3_ENDPOINT'),
    aws_access_key_id=os.getenv('SCREENSNAP_S3_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SCREENSNAP_S3_SECRET_KEY'))


def _ensure_bucket():
    try:
        _s3_client.create_bucket(Bucket='screenshots')
    except _s3_client.exceptions.BucketAlreadyOwnedByYou:
        pass


_ensure_bucket()


def put(name, data):
    _ensure_bucket()
    _s3_client.put_object(Bucket='screenshots', Key=name, Body=data)


def get(name):
    try:
        return _s3_client.get_object(Bucket='screenshots', Key=name)['Body']
    except _s3_client.exceptions.NoSuchKey:
        return None
