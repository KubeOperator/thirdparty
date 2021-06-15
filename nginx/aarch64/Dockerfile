FROM nginx:1.19.9-alpine

RUN apk del curl

RUN echo > /etc/apk/repositories && echo -e "https://dl-cdn.alpinelinux.org/alpine/latest-stable/main\nhttps://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories && apk update && apk upgrade

RUN wget https://kubeoperator.oss-cn-beijing.aliyuncs.com/busybox/1.33.1/arm64/busybox.tar.gz \
    && tar zxvf busybox.tar.gz -C /bin \
    && rm -rf busybox.tar.gz

RUN rm -rf /usr/lib/libpng16* /usr/lib/libncursesw* /usr/lib/libjpeg* /usr/lib/libturbojpeg*