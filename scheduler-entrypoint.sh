#!/bin/sh

set -x
set -e

python manage.py start_scheduler_service
