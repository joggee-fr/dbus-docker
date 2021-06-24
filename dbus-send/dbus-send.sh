#!/bin/sh

while [ true ]
do
    dbus-send --session --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames
    dbus-send --session --dest=com.example.HelloWorld --type=method_call --print-reply /com/example/HelloWorld org.freedesktop.DBus.Introspectable.Introspect
    dbus-send --session --dest=com.example.HelloWorld --type=method_call --print-reply /com/example/HelloWorld com.example.HelloWorld.SayHello
    sleep 10
done
