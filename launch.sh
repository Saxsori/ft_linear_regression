#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 {setup|train|precise|predict}"
  exit 1
fi

case $1 in
	setup)
    	echo "Install Python Packages..."
		pip install --upgrade pip
		pip install matplotlib numpy pillow pandas    	
    	;;
	train)
    	echo "Training Started..."
		(cd src && python train.py)
    	;;
	predict)
		echo "Predict Price..."
		(cd src && python predict.py)
		;;
	precise)
		echo "Calculate the precision of my Algorithm..."
		(cd src && python precision.py)
		;;
	*)
		echo "Invalid option: $1"
		echo "Usage: $0 {setup|train|precise|predict}"
		exit 1
    	;;
esac

exit 0
