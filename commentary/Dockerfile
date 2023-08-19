FROM ubuntu:18.04 AS commentary-server

RUN useradd -m -d /home/ctf -u 12345 ctf
WORKDIR /home/ctf

RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN pip3 install flask

WORKDIR /app

COPY . .

RUN chown -R root:root /app

USER ctf
EXPOSE 9999
RUN ["python3", "server.py"]