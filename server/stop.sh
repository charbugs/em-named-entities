#!/bin/bash

MARKER_NAME=em-named-entities

cd /home/charbugs/github/$MARKER_NAME/server
uwsgi --stop /tmp/$MARKER_NAME.pid
