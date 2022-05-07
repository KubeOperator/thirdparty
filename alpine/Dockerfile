FROM yobasystems/alpine:3.15.4

ENV ENV="/root/.ashrc"
RUN echo 'umask 0027' >> /root/.ashrc
RUN deluser sync || true && \
    deluser shutdown || true && \
    deluser halt || true && \
    deluser operator || true

RUN echo > /etc/apk/repositories && \
    echo -e "https://dl-cdn.alpinelinux.org/alpine/v3.16/main\nhttps://dl-cdn.alpinelinux.org/alpine/v3.16/community" >> /etc/apk/repositories && \
    apk update && \
    apk upgrade

CMD ["/bin/sh"]
