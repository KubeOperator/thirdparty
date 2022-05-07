FROM alpine:3.15.4

ARG NEXUS_VERSION=3.38.1-01
ARG JAVA_ALPINE_VERSION=8.302.08-r2

RUN echo > /etc/apk/repositories && echo -e "https://dl-cdn.alpinelinux.org/alpine/v3.16/main\nhttps://dl-cdn.alpinelinux.org/alpine/v3.15/community" >> /etc/apk/repositories && apk update && apk upgrade

ENV LANG=C.UTF-8 \
  JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk \
  PATH=${PATH}:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin \
  NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz \
  NEXUS_HOME=${SONATYPE_DIR}/nexus \
  NEXUS_DATA=/nexus-data \
  NEXUS_CONTEXT='' \
  SONATYPE_DIR=/opt/sonatype \
  SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work

RUN { \
    echo '#!/bin/sh'; \
    echo 'set -e'; \
    echo; \
    echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
  } > /usr/local/bin/docker-java-home \
  && chmod +x /usr/local/bin/docker-java-home

RUN set -x \
  && apk add --no-cache \
    openjdk8="$JAVA_ALPINE_VERSION" \
  && [ "$JAVA_HOME" = "$(docker-java-home)" ]

RUN mkdir -p ${NEXUS_HOME} \
  && apk add --no-cache curl tar shadow \
  && curl --fail --silent --location --retry 3 \
    ${NEXUS_DOWNLOAD_URL} \
  | gunzip \
  | tar x -C ${NEXUS_HOME} --strip-components=1 nexus-${NEXUS_VERSION} \
  && chown -R root:root ${NEXUS_HOME} \
  && apk del curl tar

RUN sed \
    -e '/^nexus-context/ s:$:${NEXUS_CONTEXT}:' \
    -i ${NEXUS_HOME}/etc/nexus-default.properties

RUN useradd -r -u 200 -m -c "nexus role account" -d /var/cache/nexus -s /bin/false nexus \
  && mkdir -p ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp ${SONATYPE_WORK} \
  && ln -s ${NEXUS_DATA} ${SONATYPE_WORK}/nexus3 \
  && chown -R nexus:nexus ${NEXUS_DATA} \
  && chown -R nexus:nexus /var/cache/nexus \
  && chmod -R g+w /var/cache/nexus

VOLUME ${NEXUS_DATA}

EXPOSE 8081
USER nexus
WORKDIR ${NEXUS_HOME}

ENV JAVA_MAX_MEM=1200m \
  JAVA_MIN_MEM=1200m \
  EXTRA_JAVA_OPTS="" \
  ENV="/var/cache/nexus/.ashrc"

RUN echo 'umask 0027' >> /var/cache/nexus/.ashrc

CMD ["bin/nexus", "run"]