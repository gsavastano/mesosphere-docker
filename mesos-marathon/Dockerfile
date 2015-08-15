FROM xdevelsistemas/mesosphere-docker:latest

## MARATHON ##
ADD https://downloads.mesosphere.io/marathon/v0.10.0/marathon-0.10.0.tgz /tmp/marathon.tgz
RUN mkdir -p /opt/marathon && tar xzf /tmp/marathon.tgz -C /opt/marathon --strip=1 && rm -f /tmp/marathon.tgz

EXPOSE 8080
WORKDIR /opt/marathon
CMD ["--help"]
ENTRYPOINT ["/opt/marathon/bin/start"]
