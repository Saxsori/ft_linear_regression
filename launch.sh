#!/bin/bash

VENV="src/venv"

if [ -z "$1" ]; then
	help
fi

help() {
	echo "Usage: $0 {setup|train|precise|predict|clean}"
	exit 1
}

create_venv() {
    if ! command -v virtualenv &> /dev/null; then
        echo "virtualenv is not installed. Installing..."
        python3 -m pip install --user virtualenv
        echo "virtualenv installation complete."
    fi
    
    if [ -d "$VENV" ]; then
        echo "Virtual environment '$VENV' already exists. Aborting."
        return 1
    fi

    python3 -m venv "$VENV"
    source "./$VENV/bin/activate"
}

remove_venv() {
	echo "Cleaning up the environment..."

    if [ ! -d "$VENV" ]; then
        echo "Virtual environment '$VENV' not found."
        return 1
    fi

    deactivate
    rm -rf "$VENV"
}

install_packages() {
	echo "Install Python Packages..."
	pip install --upgrade pip
	pip install matplotlib numpy pillow pandas    	
}

train () {
	echo "Training Started..."
	(cd src && python train.py) 	
}

predict () {
	echo "Predict Price..."
	(cd src && python predict.py)	
}

precise () {
	echo "Calculate the precision of my Algorithm..."
	(cd src && python precision.py)	
}

case "$1" in
    "setup")
        create_venv    	
        ;;
	"install")
		install_packages
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
        remove_venv 
        ;;
    *)
		help
        ;;
esac
