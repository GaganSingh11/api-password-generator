# Password on Demand API

#### First Clone this repo using git

```
git clone git@github.com:GaganSingh11/api-password-generator.git
```

Once cloned the repo make sure you are inside the 
api-password-generator directory :)

```
$ cd api-password-generator 
```

### Setup the project using docker and docker-compose

- This project has docker-compose file which can be used to setup the environment locally.
  To Download the docker engine and docker-compose in your system please refer the below link

  - [Docker Install Doc](https://docs.docker.com/install/)
  - [Docker Compose](https://docs.docker.com/compose/install/)


- After installing docker in your local machine please run this in your command line for development environment

```cmd
$ docker-compose -f docker-compose-dev.yml up -d
```
__OR__
- After installing docker in your local machine please run this in your command line for production environment

```cmd
$ docker-compose -f docker-compose-prod.yml up -d
```

- To check if containers are running please run

```
$ docker ps
```

It should show something like this

```
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS          PORTS                  NAMES
77a102ac1733   gaganvorn/password-generator:latest   "uvicorn app.main:ap…"   15 minutes ago   Up 20 seconds   0.0.0.0:80->8000/tcp   password-generator_api_1
```

    - password-generator_api_1 is the password generator project using FastAPI running on port 80.

To stop and delete containers.

```
$ docker-compose -f docker-compose-dev.yml down
```
__OR__

```
$ docker-compose -f docker-compose-prod.yml down
```

This project is using pytest python unittest framework

To run the tests (before please bring containers running)

```
$ docker exec password-generator_api_1 "pytest"

```

To check swagger document please click (before please bring containers running) [swagger prod](http://localhost:80/docs/) __OR__ [swagger dev](http://localhost:4000/docs/)

### Setup the local virtual environment for development purposes.

- This project uses some features which are only available in python3.9+ so please install python3.9 or higher in your system

  - [python download](https://www.python.org/downloads/)

- Once the python3.9+ is setup in your system, highly recommend to use virtual env instead of global python interpreter. [venv](https://docs.python.org/3/library/venv.html)

> To create virtual python environment

```
$python3.9 -m venv env
```

> To activate virtual env

```
$ source env/bin/activate
```

> Now, install requirements using pip

```
(env)$ pip install -r requirements.txt
```

Once everything setup to check if the project is setup correctly please run this command

```
(env)$ uvicorn app.main:app --reload  
```

To run the test case

```
(env)$ pytest -v
```

To check swagger document please click [swagger](http://localhost:8000/docs/)

### Container Registry

To check all docker images in container registry click [dockerhub](https://hub.docker.com/repository/docker/gaganvorn/password-generator)


