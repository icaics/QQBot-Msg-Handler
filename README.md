# Kalina [QQBot-GF-Kalina]

### Based on [pandolia / qqbot](https://github.com/pandolia/qqbot)

## Usage

* Clone

>1. Make **workspace** `mkdir /docker`
>2. Clone repo to **workspace**
>3. Enter repo `cd qqbot-gf-kalina`

* Docker

>1. Get docker python:3.5: `docker pull python:3.5`
>2. Use **Dockerfile** build image named **qqbot-gf-kalina**: `docker build -t qqbot-gf-kalina .`
>3. Pay attention to the `.` in setp 2

* Config File

>1. Make folder **config** for qqbot config file: `mkdir config`
>2. Put ``v2.3.conf`` into **config** folder
>3. Prepare config file **BEFORE** run `./startup.sh`

* Run

>Run `./startup.sh` to **RUN QQBot**

* Update

>Run `./update.sh` to **update**

## Instructions for v2.3.conf

* `User Profile name` in .conf is `kalina`

* `QQBot-term Server` port in docker is `"termServerPort" : 8000`

* `QR Code login` port in docker is `"httpServerPort" : 443`

* `PluginPath` in docker is `"pluginPath" : "/qqbot/"`

* `Plugins` in docker is `"plugins" : ['Define', 'Kalina', 'SchedRestart']`

## Thanks

* **Build simulator** data from [IOP Corporation Manufactoring Statistics](http://gfdb.baka.pw/statistician.html)
