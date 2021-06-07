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
docker exec -it youtube-video-api_app_1 bash   <youtube-video-api_app_1 --> your container name>
conda activate youtube
conda install conda-build
conda activate youtube
conda develop {{pwd}}

python  core/batch/youtube-data/dump_videos.py

````

###SWAGGER

[Swagger Docs](https://0.0.0.0:5000/docs) Runs on host specified here port 5000


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
