FROM centos:7

RUN yum install -y wget tar  gzip gcc gcc-c++ glibc-headers python3

#make 4.2.1

WORKDIR /build

RUN wget http://ftp.gnu.org/gnu/make/make-4.2.1.tar.gz

RUN tar -zvxf make-4.2.1.tar.gz

RUN /build/make-4.2.1

RUN ../configure && ./build.sh

RUN mv make /usr/local/bin

WORKDIR /build

RUN rm -fr *


# gcc 9.2.0
WORKDIR /build

RUN wget https://ftp.gnu.org/gnu/gcc/gcc-9.2.0/gcc-9.2.0.tar.gz
RUN tar -zvxf gcc-9.2.0.tar.gz

WORKDIR /build/gcc-9.2.0/contrib

RUN ./download_prerequisites

WORKDIR /build/gcc-9.2.0/build

RUN ../configure  --enable-bootstrap --enable-checking=release --enable-languages=c,c++ --disable-multilib checking=release --enable-languages=c,c++ --disable-multilib

RUN make && make install

WORKDIR /build

RUN rm -fr *


# glibc 2.33

WORKDIR /build

RUN wget http://ftp.gnu.org/gnu/glibc/glibc-2.33.tar.gz

RUN tar -zvxf glibc-2.33.tar.gz

WORKDIR /build/glibc-2.33/build

RUN ../configure   --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin

RUN make && make install

RUN rm -fr *


# openssl 1.1.1k

WORKDIR /build

RUN wget https://www.openssl.org/source/openssl-1.1.1k.tar.gz

RUN tar -zvxf openssl-1.1.1k.tar.gz

WORKDIR /build/openssl-1.1.1k

RUN ./config && make &&make install

RUN rm -fr *




