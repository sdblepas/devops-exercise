## Overview

This repository takes [Flaskex](https://github.com/anfederico/flaskex) containerizes it.
Also includes a CircleCI pipeline which stores the docker images into Dockerhub and Artifactory.
Additionally the CircleCI pipeline tests the application and stores the tests results in Artifactory.

## Setup
```
git clone https://github.com/Lexarity/devops-exercise
cd devops-exercise
docker compose up
```

## Requirements For CICD

[Jfrog account](https://jfrog.com/start-free/).
[CircleCI account](https://circleci.com/signup/).
[Dockerhub account](https://hub.docker.com/signup).
Github account + forking the repo.

## CICD
In order to setup the CICD pipeline, make sure to answer all the requirements first.

### CircleCI 
Login to your CircleCI account, sync your github account and choose the appropriate repository.
Make sure to select the main branch when choosing to create a pipeline.

It should initally fail as we haven't set the appropriate environment variables.
### Artifactory

Make sure to have created a Jfrog account and have selected your JFrog platform to be hosted on cloud.

Make sure to copy the API_KEY for later usage.


### Pipeline Construction


In order to successfully run the pipeline please add the following environment variables:

1. Navigate to the created project and click on Project Settings
2. Click on Environment Variables and add the following:
```
ARTIFACTORY_URL - Artifactory URL - example - devopsexercise.jfrog.io.
ARTIFACTORY_REPO - Designated Artifactory repo - example - devops-exercise-docker.
ARTIFACTORY_API_KEY - API_KEY for the account - retrieve it by going to the profile.
ARTIFACTORY_USERNAME - Username for Artifactory.
DOCKERHUB_PASSWORD - Password for Dockerhub.
DOCKERHUB_USERNAME - Username for Dockerhub.
IMAGE_NAME - Designated image name.
```

3. Head back towards the pipeline and trigger it manually. 
4. Your container is now present in both Artifactory and in Dockerhub.

In order to ensure the CICD process works as intended - the docker-compose.yml will need to be updated accordingly. 

We will need to add the usage of our newly pushed image located in Dockerhub:

```
image: <Dockerhub Username>:<Image Name>
```

For an example the docker-compose.yml file will be the following:
```

version: "3.9"
services:
  web:
    build: .
    ports:
      - 5000:5000
    volumes:
      - .:/service
    image: lexarity/devopsexercise
```

Now you will be able to run Flaskex on a containerized environment using docker compose.
Additionally, the CircleCI pipeline will be triggered upon push to branch. 


## Features
[Flaskex](https://github.com/anfederico/Flaskex)


### Author
Tal Barnoy
