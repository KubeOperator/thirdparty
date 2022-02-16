FROM nginx:1.21.6-alpine

RUN apk del curl

RUN apk update && apk upgrade

RUN rm -rf /usr/lib/libpng16* /usr/lib/libncursesw* /usr/lib/libjpeg* /usr/lib/libturbojpeg*