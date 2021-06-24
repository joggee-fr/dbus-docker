from gi.repository import GObject
import dbus
import dbus.service

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)


OPATH = "/com/example/HelloWorld"
IFACE = "com.example.HelloWorld"
BUS_NAME = "com.example.HelloWorld"


class Example(dbus.service.Object):
    def __init__(self):
        bus = dbus.SessionBus()
        bus.request_name(BUS_NAME)
        bus_name = dbus.service.BusName(BUS_NAME, bus=bus)
        dbus.service.Object.__init__(self, bus_name, OPATH)

    @dbus.service.method(dbus_interface=IFACE,
                         in_signature="", out_signature="s")
    def SayHello(self):
        print("SayHello method called")
        return "Hello World!"


if __name__ == "__main__":
    a = Example()
    loop = GLib.MainLoop()
    print("Dbus service started")
    loop.run()
