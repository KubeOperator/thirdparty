FROM nginx:1.19.9-alpine

RUN apk del curl

RUN echo > /etc/apk/repositories && echo -e "https://dl-cdn.alpinelinux.org/alpine/latest-stable/main\nhttps://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories && apk update && apk upgrade

RUN rm -rf /usr/lib/libpng16* /usr/lib/libncursesw* /usr/lib/libjpeg* /usr/lib/libturbojpeg*