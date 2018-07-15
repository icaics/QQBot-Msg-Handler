#!/bin/sh

echo [INFO] Updating ...
git pull origin master

echo [INFO] Restarting docker ...
docker restart qqbot-gf-kalina

echo [INFO] Done.
