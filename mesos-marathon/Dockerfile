FROM debian:wheezy

# Install dependancies
RUN apt-get -y update && apt-get -y install lsb-release
RUN DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]'); CODENAME=$(lsb_release -cs); echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" |  tee /etc/apt/sources.list.d/mesosphere.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF



RUN apt-get update
RUN apt-get install --assume-yes mesos python-software-properties curl default-jdk

## MARATHON ##
ADD https://downloads.mesosphere.io/marathon/v0.8.1/marathon-0.8.1.tgz /tmp/marathon.tgz
RUN mkdir -p /opt/marathon && tar xzf /tmp/marathon.tgz -C /opt/marathon --strip=1 && rm -f /tmp/marathon.tgz

EXPOSE 8080
WORKDIR /opt/marathon
CMD ["--help"]
ENTRYPOINT ["/opt/marathon/bin/start"]
