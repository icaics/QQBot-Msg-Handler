#!/bin/sh

docker run --name qqbot -p 443:443 -p 8000:8000 -v ./plugins:/qqbot -v ./config:/root/.qqbot-tmp/ -d --restart=always qqbot /qqbot.sh
