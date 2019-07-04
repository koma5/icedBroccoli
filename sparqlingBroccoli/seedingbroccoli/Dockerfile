FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    python \
    python-pip


COPY * /

RUN npm install

RUN pip install -r requirements.txt

CMD bash hotShit.sh
