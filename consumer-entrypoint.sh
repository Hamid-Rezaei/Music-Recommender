#!/bin/sh

set -x
set -e

python manage.py start_consumer_service
