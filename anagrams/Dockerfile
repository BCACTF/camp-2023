FROM --platform=linux/amd64 ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9 AS build

RUN apt-get update -y && apt-get install -y gcc && apt-get install -y wget && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

COPY main.c .
RUN gcc -o anagrams main.c

RUN wget -qO /tmp/ynetd.zip https://github.com/rwstauner/ynetd/releases/download/v0.14/ynetd-linux-amd64.zip \
  && unzip -d ynetd /tmp/ynetd.zip \
  && rm -f /tmp/ynetd.zip


FROM --platform=linux/amd64 ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9

RUN useradd -m -d /home/ctf -u 12345 ctf
WORKDIR /home/ctf

RUN chmod +x ynetd

COPY --from=build anagrams anagrams
COPY --from=build ynetd ynetd
COPY flag.txt .
COPY main.c main.c

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 9999
CMD ./ynetd -p 9999 ./anagrams