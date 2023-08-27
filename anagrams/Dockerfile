FROM --platform=linux/amd64 ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9 AS build

RUN apt-get install -y && apt-get update -y && \
  apt-get upgrade -y && apt-get install -y gcc wget unzip && rm -rf /var/lib/apt/lists/*

COPY main.c .
RUN gcc -o anagrams main.c

RUN wget -O ynetd.c https://raw.githubusercontent.com/johnsonjh/ynetd/master/ynetd.c \
  && gcc -o ynetd ynetd.c \
  && rm -f /tmp/ynetd.zip

FROM --platform=linux/amd64 ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9 AS deploy

RUN useradd -m -d /home/ctf -u 12345 ctf
WORKDIR /home/ctf


COPY --from=build anagrams anagrams
COPY --from=build ynetd ynetd
RUN chmod +x ynetd
COPY flag.txt .
COPY main.c main.c

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 9999
CMD ./ynetd -p 9999 ./anagrams