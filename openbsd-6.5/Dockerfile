FROM debian:buster-slim AS build
RUN apt-get update && apt-get -y --no-install-recommends install \
      gcc make \
      libc-dev libncurses-dev \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY checksum checksum
ADD https://github.com/ibara/mg/releases/download/mg-6.5/mg-6.5.tar.gz mg.tar.gz
RUN sha256sum -c checksum
RUN mkdir mg && tar -C mg --strip-components 1 -xf mg.tar.gz
WORKDIR /build/mg
RUN ./configure
RUN make
RUN make install

FROM debian:buster-slim
RUN apt-get update && apt-get -y --no-install-recommends install \
      libncurses6 \
 && rm -rf /var/lib/apt/lists/*
COPY --from=build /usr/local/ /usr/local/
CMD ["mg"]
