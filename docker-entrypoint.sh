#!/bin/sh

. /venv/bin/activate

cd /usr/src/app

python ./nerdascii.py "$@"
