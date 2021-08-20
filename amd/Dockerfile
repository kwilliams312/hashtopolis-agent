FROM rocm/rocm-terminal 
USER root
RUN sudo apt-get update && sudo apt-get install -y \
  zip \
  git \
  python3 \
  python3-psutil \
  python3-requests \
  python3-setuptools \
  p7zip \
  python3-pip \
  pciutils \
  curl 

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
