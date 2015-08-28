FROM centos:7
MAINTAINER Clayton Santos da Silva <clayton@xdevel.com.br>

# Add EPEL repository
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum clean all && \
    rpm --rebuilddb
#install pre-req and add mesos
RUN yum install -y curl; yum upgrade -y; yum update -y;  yum clean all; \
    rpm -i http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm && yum -y install mesos-0.23.0
#install java
ENV	LANG en_US.UTF-8
ENV	LC_ALL en_US.UTF-8
ENV JDK_VERSION 8u60
ENV JDK_BUILD_VERSION b27
RUN curl -LO "http://download.oracle.com/otn-pub/java/jdk/$JDK_VERSION-$JDK_BUILD_VERSION/jdk-$JDK_VERSION-linux-x64.rpm" -H 'Cookie: oraclelicense=accept-securebackup-cookie' && rpm -i jdk-$JDK_VERSION-linux-x64.rpm; rm -f jdk-$JDK_VERSION-linux-x64.rpm; yum clean all
ENV JAVA_HOME /usr/java/default

#install npm
RUN yum -y install nodejs npm && \
#install awscli
    yum install -y python-pip git && \
    pip install awscli

# http://docs.docker.com/installation/centos/
#RUN curl -sSL https://get.docker.com/ | sh
RUN  yum install -y docker-1.6.2-*

CMD ["/usr/sbin/mesos-slave"]

ENV MESOS_WORK_DIR /tmp/mesos
ENV MESOS_CONTAINERIZERS docker,mesos

# https://mesosphere.github.io/marathon/docs/native-docker.html
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins

#add worker on root
ADD s3_worker.py /

VOLUME /tmp/mesos
