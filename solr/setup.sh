#!/usr/bin/env bash
set -e

bin/solr create_core -c reddit_recommender
bin/post -c reddit_recommender data/*