FROM python:3

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    gcc libdbus-1-dev libdbus-glib-1-dev libgirepository1.0-dev && \
    pip3 install dbus-python PyGObject

COPY service.py /tmp/service.py

ENV DBUS_SESSION_BUS_ADDRESS=tcp:host=dbus-daemon,bind=*,port=3000,family=ipv4

ENTRYPOINT python3 -u /tmp/service.py
