FROM centos:8

RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN mkdir ~/fakelogger
WORKDIR ~/fakelogger
RUN yum update -y
RUN yum install python39 -y
RUN yum install wget -y
RUN wget https://raw.githubusercontent.com/omkardamame/fakelogger/master/fakelogger.py

ENTRYPOINT python3 fakelogger.py