FROM alpine

COPY dbus-send.sh /tmp

RUN apk update && \
    apk add dbus && \
    chmod a+x /tmp/dbus-send.sh

ENV DBUS_SESSION_BUS_ADDRESS=tcp:host=dbus-daemon,bind=*,port=3000,family=ipv4

ENTRYPOINT /tmp/dbus-send.sh
