#!/bin/sh

docker run --name qqbot-gf-kalina -p 8000:8000 -p 8001:8001 -v /docker/qqbot-gf-kalina/plugins:/qqbot -v /docker/qqbot-gf-kalina/config:/root/.qqbot-tmp/ -d --restart=always qqbot-gf-kalina /qqbot.sh
