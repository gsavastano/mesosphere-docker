FROM xdevelsistemas/mesosphere-docker:latest

RUN echo in_memory | dd of=/etc/mesos-slave/registry

# Not exposing port b/c you have to run the master in bridge net mode
EXPOSE 5050

ENTRYPOINT ["mesos-slave"]
