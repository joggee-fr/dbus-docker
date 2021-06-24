FROM alpine

RUN apk update && \
    apk add dbus strace

COPY dbus.conf /usr/share/dbus-1/session.conf

ENTRYPOINT dbus-daemon --session --nopidfile --nofork --print-address --nosyslog
