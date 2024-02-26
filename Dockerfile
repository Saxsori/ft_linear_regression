# Use Debian as the base image
FROM debian:latest

RUN apt update && apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz && tar -xvf Python-3.10.0.tgz

WORKDIR /Python-3.10.0

RUN ./configure --enable-optimizations && make -j 2 && make altinstall

# req for Moudule 0
RUN pip3.10 install tqdm flake8 && alias norminette=flake8 

# req for Module 1
RUN apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev 

RUN pip3.10 install matplotlib pycairo PyGObject numpy

COPY ./src /src

WORKDIR /src

CMD [ "/bin/bash" ]