FROM yobasystems/alpine:3.14.0-aarch64

LABEL maintainer="KubeOperator <kubeoperator@fit2cloud.com>" \
    architecture="arm64v8/aarch64" \
    mariadb-version="10.5.11" \
    alpine-version="3.14.0" \
    org.opencontainers.image.title="alpine-mariadb" \
    org.opencontainers.image.description="MariaDB Docker image running on Alpine Linux" \
    org.opencontainers.image.authors="KubeOperator <kubeoperator@fit2cloud.com>" \
    org.opencontainers.image.vendor="KubeOperator" \
    org.opencontainers.image.version="v10.5.11"

RUN apk add --no-cache mariadb mariadb-client mariadb-server-utils pwgen && \
    rm -f /var/cache/apk/*

RUN rm -rf /usr/lib/libcurl* /usr/lib/libncursesw*

RUN wget https://kubeoperator.oss-cn-beijing.aliyuncs.com/busybox/1.33.1/arm64/busybox.tar.gz \
    && tar zxvf busybox.tar.gz -C /bin \
    && rm -rf busybox.tar.gz

ADD files/run.sh /scripts/run.sh
RUN mkdir /docker-entrypoint-initdb.d && \
    mkdir /scripts/pre-exec.d && \
    mkdir /scripts/pre-init.d && \
    chmod -R 755 /scripts

EXPOSE 3306

VOLUME ["/var/lib/mysql"]

ENTRYPOINT ["/scripts/run.sh"]
