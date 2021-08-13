<h1 align="center"> All in one project </h1> <br>

<p align="center">
  Using Python microservices allows you to break up your apps into smaller parts that communicate with each other. This can make it simpler to scale the application based on the traffic. Also, the separation of concerns makes it easier to work on just one part of the app at a time..
</p>


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Testing](#testing)
- [API](#requirements)
- [Acknowledgements](#acknowledgements)




## Introduction

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e91606af4a364076a7058c5ea1c006a8)](https://www.codacy.com/app/joneubank/microservice-template-java?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=overture-stack/microservice-template-java&amp;utm_campaign=Badge_Grade)
[![CircleCI](https://circleci.com/gh/overture-stack/microservice-template-java/tree/master.svg?style=shield)](https://circleci.com/gh/overture-stack/microservice-template-java/tree/master)

TODO: Replace with introduction

## Features
TODO: Description of features
* web server features


## Requirements
The application can be run locally or in a docker container, the requirements for each setup are listed below.


### Local
* [Python](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/download/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)


### Rabbitmq
* [RabbitMQ](https://www.rabbitmq.com/download.html)

### Docker
* [Docker](https://www.docker.com/get-docker)


The default value in the docker_compose.yml file is set to  running locally on its default port `8000`.

### Run Local
```bash
$ docker-compose -f docker-compose.yml up --build
```

Application will run by default on port `8000`
Api will be run by default on port `8001`

Configure the port by changing `port` in docker_compose.yml


### Run Docker

First build the image:
```bash
$ docker-compose build
```

When ready, run it:
```bash
$ docker-compose up
```


## Testing
TODO: Additional instructions for testing the application.


## API
TODO: API Reference with examples

## Acknowledgements
TODO: Show folks some love.
