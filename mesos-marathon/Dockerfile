FROM xdevelsistemas/mesosphere-docker:latest

RUN apt-get -y install marathon

EXPOSE 8080
WORKDIR /opt/marathon
CMD ["--help"]
ENTRYPOINT ["/opt/marathon/bin/start"]
