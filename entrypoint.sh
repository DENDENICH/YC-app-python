#!/bin/sh

set -e
echo "Waiting for app..."
sleep 2
cd app

exec python3 main.py