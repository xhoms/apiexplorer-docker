#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push tidr/apiexplorer
docker push tidr/apiexplorer_nginx
