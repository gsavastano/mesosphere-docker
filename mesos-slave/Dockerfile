FROM xdevelsistemas/mesosphere-docker:latest

RUN echo in_memory | dd of=/etc/mesos-slave/registry

RUN \
  apt-get install -y unzip && \
  apt-get clean

# Not exposing port b/c you have to run the master in bridge net mode
EXPOSE 5051

ENTRYPOINT ["mesos-slave"]
