#!/bin/bash


image_name="ft_linear_regression"

container_name="ft_linear_regression"

if ! docker image ls | grep "$image_name"; then
	docker build -t "$image_name" .
fi

if ! docker container ls -a | grep "$container_name" ; then
	docker run -d -it --rm --name "$container_name" -v ./src:/src "$image_name"
fi

docker exec -it "$container_name" /bin/bash