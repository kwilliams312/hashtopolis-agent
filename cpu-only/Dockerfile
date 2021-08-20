FROM ubuntu:18.04

RUN apt update && apt install -y \
  zip \
  git \
  python3 \
  python3-psutil \
  python3-requests \
  python3-setuptools \
  p7zip \
  python3-pip \
  pciutils \
  curl && \
  rm -rf /var/lib/apt/lists/*

RUN pip3 install \
  py7zr

CMD mkdir /root/htpclient

WORKDIR /root/htpclient

RUN cp /usr/bin/7zr /root/htpclient

RUN git clone https://github.com/s3inlc/hashtopolis-agent-python.git && \
  cd hashtopolis-agent-python && \
  ./build.sh && \
  mv hashtopolis.zip ../ && \
  cd ../ && rm -R hashtopolis-agent-python

CMD ["python3", "hashtopolis_agent_startup.py"]
