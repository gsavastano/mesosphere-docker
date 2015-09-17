FROM xdevelsistemas/centos-env:mesos-req-env
MAINTAINER Clayton Santos da Silva <clayton@xdevel.com.br>

#install pre-req and add mesos
RUN yum install -y curl; yum upgrade -y; yum update -y;  yum clean all; \
    yum -y install wget gcc gcc-c++ make flex bison gperf ruby openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel libpng-devel libjpeg-devel; \
    rpm -i http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm && yum -y install mesos-0.23.0


# http://docs.docker.com/installation/centos/
#RUN curl -sSL https://get.docker.com/ | sh
RUN  yum install -y docker-1.6.2-*

ENTRYPOINT ["/usr/sbin/mesos-slave"]

ENV MESOS_WORK_DIR /tmp/mesos
#ENV MESOS_CONTAINERIZERS docker,mesos
ENV MESOS_CONTAINERIZERS mesos

# https://mesosphere.github.io/marathon/docs/native-docker.html
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT 5mins

#add worker on root
ADD s3_worker.py /

VOLUME /tmp/mesos
