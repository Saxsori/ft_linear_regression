FROM debian:latest

#install python3

RUN apt-get update && apt-get install -y python3 python3-pip

CMD ["/bin/bash"]
