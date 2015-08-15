FROM debian:jessie

ENV VERSION 0.23.0
ENV PKG_RELEASE 1.0


# Install dependancies
RUN apt-get update && apt-get -y install lsb-release && \
    apt-get install -y openssh-server &&\
    apt-get install -y sudo &&\
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >> /etc/apt/sources.list && \
    TMPNAME=$(tempfile) && \
    apt-get update >> /dev/null 2> $TMPNAME && \
    PGPKEY=`cat $TMPNAME | cut -d":" -f6 | cut -d" " -f3` && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $PGPKEY && \
    rm $TMPNAME && \
    apt-get update && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive  apt-get install -yq oracle-java7-installer oracle-java7-set-default
#install docker
RUN echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list && \
    apt-get -y update
RUN apt-get install -y docker.io && \
    apt-get -y install curl python-setuptools python-pip python-dev python-protobuf
#install mesos
RUN curl -s -O http://downloads.mesosphere.io/master/debian/8/mesos_${VERSION}-${PKG_RELEASE}.debian81_amd64.deb && \
    dpkg --unpack mesos_${VERSION}-${PKG_RELEASE}.debian81_amd64.deb
#Clean up apt-repository
#RUN apt-get clean && \
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
