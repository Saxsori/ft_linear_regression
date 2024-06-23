#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 {setup|train|precise|predict|clean}"
  exit 1
fi

VENV_DIR="venv"

case $1 in
	setup)
    	echo "Install Python Packages..."
		if [ ! -d "$VENV_DIR" ]; then
            python3 -m venv "$VENV_DIR"
        fi
        
		source "$VENV_DIR/bin/activate"

		pip install --upgrade pip
		pip install matplotlib numpy pillow pandas    	
    	;;
	train)
    	echo "Training Started..."
        if [ -d "$VENV_DIR" ]; then
            source "$VENV_DIR/bin/activate"
            (cd src && python train.py)
        else
            echo "Virtual environment not found. Please run '$0 setup' first."
            exit 1
        fi    	
		;;
	predict)
		echo "Predict Price..."
        if [ -d "$VENV_DIR" ]; then
            source "$VENV_DIR/bin/activate"
            (cd src && python predict.py)
        else
            echo "Virtual environment not found. Please run '$0 setup' first."
            exit 1
        fi		
		;;
	precise)
		echo "Calculate the precision of my Algorithm..."
        if [ -d "$VENV_DIR" ]; then
            source "$VENV_DIR/bin/activate"
            (cd src && python precision.py)
        else
            echo "Virtual environment not found. Please run '$0 setup' first."
            exit 1
        fi		
		;;
	clean)
        echo "Cleaning up the environment..."
        if [ -d "$VENV_DIR" ]; then
            rm -rf "$VENV_DIR"
            echo "Virtual environment directory deleted."
        else
            echo "Virtual environment directory not found."
        fi
        ;;
	*)
		echo "Invalid option: $1"
		echo "Usage: $0 {setup|train|precise|predict|clean}"
		exit 1
    	;;
esac

exit 0
