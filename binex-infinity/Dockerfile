FROM --platform=linux/amd64 ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9 AS build

RUN apt-get update -y && apt-get install -y gcc wget unzip && rm -rf /var/lib/apt/lists/*

RUN wget -Oynetd.c https://raw.githubusercontent.com/johnsonjh/ynetd/master/ynetd.c \
  && gcc -o ynetd ynetd.c \
  && rm -f /tmp/ynetd.zip

FROM --platform=linux/amd64 node:16

RUN useradd -m -d /home/ctf -u 12345 ctf
WORKDIR /home/ctf

COPY --from=build ynetd ynetd
COPY program.js .
COPY flag.txt .

RUN chown -R root:root /home/ctf
RUN chmod +x ./ynetd


USER ctf
EXPOSE 9999
CMD ./ynetd -p 9999 "node program.js"