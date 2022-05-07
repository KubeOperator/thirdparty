FROM kubeoperator/alpine:3.15.4

RUN apk add --no-cache mariadb mariadb-client mariadb-server-utils pwgen && \
    rm -rf /var/cache/apk/* /usr/bin/perl /usr/bin/test-connect-t /usr/bin/mariadb-embedded /usr/lib/libbrotlicommon.so.* /usr/lib/libmenuw.so.* && \
    find / -regex '.*\.pem\|.*\.crt\|.*\.p12\|.*\.pfx\|.*\gitignore' -type f|xargs rm -rf

ADD files/run.sh /scripts/run.sh
RUN mkdir /docker-entrypoint-initdb.d && \
    mkdir /scripts/pre-exec.d && \
    mkdir /scripts/pre-init.d && \
    chmod -R 755 /scripts

EXPOSE 3306

VOLUME ["/var/lib/mysql"]

ENTRYPOINT ["/scripts/run.sh"]
