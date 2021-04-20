FROM alpine:3.13.5


RUN echo > /etc/apk/repositories && echo -e "https://dl-cdn.alpinelinux.org/alpine/latest-stable/main\nhttps://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories && apk update && apk upgrade

RUN apk add openjdk8 procps


ENV SONATYPE_DIR=/opt/sonatype
ENV NEXUS_HOME=${SONATYPE_DIR}/nexus \
    NEXUS_DATA=/nexus-data \
    NEXUS_CONTEXT='' \
    SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work


WORKDIR ${SONATYPE_DIR}

RUN wget https://kubeoperator.oss-cn-beijing.aliyuncs.com/nexus/image/nexus-3.30.0-01-unix.tar.gz

RUN tar -zvxf ./nexus-3.30.0-01-unix.tar.gz && mv nexus-3.30.0-01 nexus

EXPOSE 8081

USER root

VOLUME ${NEXUS_DATA}

ENV INSTALL4J_ADD_VM_PARAMS="-Xms2703m -Xmx2703m -XX:MaxDirectMemorySize=2703m -Djava.util.prefs.userRoot=${NEXUS_DATA}/javaprefs"

CMD ["./nexus/bin/nexus" ,"run"]