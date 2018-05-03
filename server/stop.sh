#!/bin/bash

MARKER_NAME=em-named-entities

cd ~/github/$MARKER_NAME/server
sudo -u www-data -g www-data pipenv run uwsgi \
	--stop /tmp/$MARKER_NAME.pid