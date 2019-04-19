# reddit-recomender

## Setup

Set the following environment variables:

* `SOLR_SERVER`
* `CORE_NAME`

```shell
docker-compose up
docker exec -it --user=solr solr_server ./setup.sh
python3 src/main.py
```

Then navigate to `http://localhost:8983`.

## Help

```shell
docker-compose up # bring up containers
docker-compose run solr_server bash # run bash on container
docker exec -it --user=solr solr_server bin/solr create_core -c CORE_NAME # create a core
docker exec -it --user=solr solr_server bin/post -c CORE_NAME dir/*
```

## How it Works

When supplied with subreddits you are already interested in, `reddit-commender`
helps you discover new subreddits.

We take the descriptions of the supplied subreddits, and find the keywords in
them. The keyword lists are then merged to make a query into Solr in which it
searches through all known subreddit descriptions for those same keywords.
Once Solr provides the results of that, we lemmatize the keywords we searched
with and the descriptions we got back. Then we determine the word overlap, and
the resulting documents are ordered by the amount of word overlap.
