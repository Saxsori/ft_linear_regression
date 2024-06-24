#!/bin/bash

image_name="ft_linear_regression"
container_name="ft_linear_regression"

if [ -z "$1" ]; then
	help
fi

help() {
	echo "Usage: $0 {setup|train|precise|predict|clean}"
	exit 1
}

setup() {
	echo "This script uses X11 forwarding to display the GUI outside the Docker container."
	echo "Please ensure that your X11 server is running on your preferred host."
	read -p "Is your X11 server ready? (yes/no): " x11_ready
	if [ "$x11_ready" != "yes" ]; then
		echo "Please start your X11 server and then run this script again."
		exit 1
	fi

	read -p "Is your X11 server launched locally or remotely? (local/remote): " display_type

	if [ "$display_type" = "local" ]; then
		export IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
	elif [ "$display_type" = "remote" ]; then
		read -p "Please enter the IP address of the host running the X11 server: " IP
	else
		echo "Invalid option: $display_type"
		exit 1
	fi


	if ! docker image ls | grep "$image_name"; then
		docker build -t "$image_name" .
	fi

	if ! docker container ls -a | grep "$container_name" ; then
		docker run -d -it --rm -e DISPLAY="${IP}:0.0" --name "$container_name" -v ./src:/src "$image_name"
	fi
}

clean() {
	echo "Cleaning up the environment..."
	docker stop "$container_name"
	docker rmi "$image_name"
}

train () {
	echo "Training Started..."
	docker exec -it "$container_name" python3.10 /src/train.py
}

predict () {
	echo "Predict Price..."
	docker exec -it "$container_name" python3.10 /src/predict.py
}

precise () {
	echo "Calculate the precision of my Algorithm..."
	docker exec -it "$container_name" python3.10 /src/precision.py
}

case "$1" in
    "setup")
        setup    	
        ;;
    "train")
		train
        ;;
    "predict")
		predict
		;;
    "precise")
		precise
        ;;
    "clean")
        clean 
        ;;
    *)
		help
        ;;
esac