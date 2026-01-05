#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python to_do_project/manage.py collectstatic --noinput
python to_do_project/manage.py migrate