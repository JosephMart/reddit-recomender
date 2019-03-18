# reddit-recomender

## Setup

```shell
docker-compose up
docker exec -it --user=solr solr_server ./setup.sh
```

Then navigate to `http://localhost:8983`.

## Help

```shell
docker-compose up # bring up containers
docker-compose run solr_server bash # run bash on container
docker exec -it --user=solr solr_server bin/solr create_core -c CORE_NAME # create a core
docker exec -it --user=solr solr_server bin/post -c CORE_NAME dir/*
```
