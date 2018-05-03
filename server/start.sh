#!/bin/bash

MARKER_NAME=em-named-entities

cd ~/github/$MARKER_NAME/server
sudo -u www-data -g www-data pipenv run uwsgi \
	--pidfile /tmp/$MARKER_NAME.pid \
	--module server:application \
	--master \
	--processes 3 \
	--socket /tmp/$MARKER_NAME.sock \
	--chmod-socket=660 \
	--vacuum \
	--logto /tmp/$MARKER_NAME.log &


