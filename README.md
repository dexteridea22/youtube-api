# Youtube Module

## Stack

- Python 3
- Flask
- Flask-Restx
- Mongoengine
- Docker
- Swagger

## Usage

[Install Docker](https://www.docker.com/products/docker-desktop) if you don't have it yet and run the container:

###Docker Setup

### Container and Image Setup
```
docker-compose build

docker-compose up

```

### Cron data load setup

````
docker exec -it youtube-api_app_1 bash   <youtube-api_app_1 --> your container name>
conda activate youtube
conda install conda-build
conda activate youtube
conda develop {{pwd}}

python  core/batch/youtube-data/dump_videos.py

````

###SWAGGER

[Swagger Docs](https://0.0.0.0:5000/docs) Runs on host specified here port 5000

###Sample mongod data load commands
```
db.youtube_videos.insert({
 "_id" : ObjectId("60bdc342edbe8a7cdf63f9df"),
 "created_at" : ISODate("2021-06-07T12:27:06.793Z"),
 "video_id" : "bJXLT597UzM",
 "title" : "FINAL DAY || TARPALLA CRICKET CUP || 6 JUNE || 5AAB SPORTS LIVE STREAM",
 "description" : "5AAB SPORTS FEVER.",
 "published_date" : ISODate("2021-06-06T14:30:00Z"),
 "thumbnailURL" : "https://i.ytimg.com/vi/bJXLT597UzM/hqdefault.jpg"
 })
 

db.youtube_videos.insert({
 "_id" : ObjectId("60bdc342edbe8a7cdf63f9de"),
 "created_at" : ISODate("2021-06-07T12:27:06.791Z"),
 "video_id" : "A1XZJxW-l_M",
 "title" : "Funny cricket tamil | Funny cricket moments | Funny Moments happened in Cricket | Cricket Comedy",
 "description" : "Funny cricket tamil | Funny cricket moments | Funny Moments happened in Cricket | Cricket Comedy #funnycricket #cricketfunny #cricketcomedy In this video we ...",
 "published_date" : ISODate("2021-06-06T14:30:12Z"),
 "thumbnailURL" : "https://i.ytimg.com/vi/A1XZJxW-l_M/hqdefault.jpg"
 }) 
 

db.youtube_videos.insert({
"_id" : ObjectId("60bdc342edbe8a7cdf63f9db"), 
"created_at" : ISODate("2021-06-07T12:27:06.780Z"), 
"video_id" : "WmdRH1Ypxnw", 
"title" : "Best Of Euro #2,  Equipe de France I FFF 2021", 
"description" : "Retrouvez les meilleurs moments de la deuxième semaine de rassemblement des Bleus de Didier Deschamps en vue de la préparation à l'Euro. Tous les buts ...", 
"published_date" : ISODate("2021-06-06T15:00:11Z"), 
"thumbnailURL" : "https://i.ytimg.com/vi/WmdRH1Ypxnw/hqdefault.jpg" 
}) 
 
```

## SETUP WITHOUT DOCKER


### Install Anaconda
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```


### Install Mongo
```
brew install  mongodb-community@4.4
brew services restart mongodb-community
```

### Setup Environment
```
conda env create -f /home/{{folder}}/environment.yml
conda develop {{pwd}}
```


### Conda useful commands:
```
Clone Environment: conda env export > environment.yml --no-builds
Update Environment: conda env update --file environment.yml

```

### Cron jobs:
```
Conda activate {environment}
python  core/batch/yt_data/dump_videos.py
```


