FROM xdevelsistemas/mesosphere-docker:latest

#zookeeper conf
RUN echo 1 | dd of=/var/lib/zookeeper/myid



RUN echo in_memory | dd of=/etc/mesos-master/registry

# Not exposing port b/c you have to run the master in bridge net mode
EXPOSE 5050

ENTRYPOINT ["mesos-master"]
