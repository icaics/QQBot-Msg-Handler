# Kalina [QQBot-GF-Kalina]

### Based on [pandolia / qqbot](https://github.com/pandolia/qqbot)

## Usage

* Clone

> 1. Make **workspace** `mkdir /docker`
> 1. Clone repo to **workspace**
> 1. Enter repo `cd qqbot-gf-kalina`

* Docker

> 1. Get docker python:3.5: `docker pull python:3.5`
> 1. Use **Dockerfile** build image named **qqbot-gf-kalina**: `docker build -t qqbot-gf-kalina .`
> 1. Pay attention to the `.` in setp 2

* Config File

> 1. Make folder **config** for qqbot config file: `mkdir config`
> 1. Put ``v2.3.conf`` into **config** folder
> 1. Prepare config file **BEFORE** run `./startup.sh`

* Run

> Run `./startup.sh` to **RUN QQBot**

* Update

> Run `./update.sh` to **update**

## Instructions for v2.3.conf

* `User Profile name` in .conf is `kalina`

* `QQBot-term Server` port in docker is `"termServerPort" : 8000`

* `QR Code login` port in docker is `"httpServerPort" : 443`

* `PluginPath` in docker is `"pluginPath" : "/qqbot/"`

* `Plugins` in docker is `"plugins" : ['Define', 'Kalina', 'SchedRestart']`

## Tips for Data Process


```
\d*	\d*	★
["★

\d*	\d*	妖
["妖
```

```
★	
★", "

"妖精	
"妖精", "
```

```
	\d+:\d+:00	6000	2000	6000	4000	2	\d+	
", "

	\d\d:\d\d:\d\d	2500	2500	2500	2500	2	\d+	
", "
```

```
%	
"], 
```

## Thanks

* **Build simulator** data from [IOP Corporation Manufactoring Statistics](http://gfdb.baka.pw/statistician.html)
