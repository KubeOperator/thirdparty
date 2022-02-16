FROM yobasystems/alpine:3.14.0-amd64

LABEL maintainer="KubeOperator <kubeoperator@fit2cloud.com>" \
    architecture="amd64/x86_64" \
    mariadb-version="10.5.11" \
    alpine-version="3.14.0" \
    org.opencontainers.image.title="alpine-mariadb" \
    org.opencontainers.image.description="MariaDB Docker image running on Alpine Linux" \
    org.opencontainers.image.authors="KubeOperator <kubeoperator@fit2cloud.com>" \
    org.opencontainers.image.vendor="KubeOperator" \
    org.opencontainers.image.version="v10.5.11"

RUN apk update && apk upgrade

RUN apk add --no-cache mariadb mariadb-client mariadb-server-utils pwgen && \
    rm -f /var/cache/apk/*

ADD files/run.sh /scripts/run.sh
RUN mkdir /docker-entrypoint-initdb.d && \
    mkdir /scripts/pre-exec.d && \
    mkdir /scripts/pre-init.d && \
    chmod -R 755 /scripts

RUN rm -rf /usr/lib/libcurl* /usr/lib/libncursesw*

EXPOSE 3306

VOLUME ["/var/lib/mysql"]

ENTRYPOINT ["/scripts/run.sh"]
