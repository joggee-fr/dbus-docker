# Running Dbus in Docker containers
This is just a really simple project running Dbus daemon, service and client in Docker containers.

The project use `docker-compsoe` to run a `dbus-daemon` session bus listening on TCP port 3000 with no security at all.
The `dbus-service` container connects to this bus to expose the `SayHello` method. On the other side, the `dbus-send` container acts as a client.

## Usage
Build the container images:
```
$ docker-compose build
```

Run the containers:
```
$ docker-compose up
```