# Kalina [QQBot-Msg-Handler]

### Based on [pandolia / qqbot](https://github.com/pandolia/qqbot)

## Usage

* Clone

>1. Make **workspace** `mkdir /docker/qqbot`
>2. Clone repo to **workspace**

* Docker

>1. Get docker python:3.5: `docker pull python:3.5`
>2. Use **Dockerfile** build image named **qqbot**: `docker built -t qqbot .`

* WorkDir

>1. Make folder **config** for qqbot config file: `mkdir config`
>2. Put ``v2.3.conf`` into **config** folder

* Run

>User `./startup.sh` to RUN QQBot

## Instructions for v2.3.conf

* `QQBot-term Server` port in docker is `"termServerPort" : 8000`

* `QR Code login` port in docker is `"httpServerPort" : 443`

* `PluginPath` in docker is `"pluginPath" : "/qqbot/"`

## Thanks

* **Build simulator** data from [IOP Corporation Manufactoring Statistics](http://gfdb.baka.pw/statistician.html)
