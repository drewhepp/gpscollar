import machine
import socket

from network import WLAN

ADDR='192.168.0.100'
SUBNET_MASK='255.255.255.0'
DEFAULT_GATEWAY='192.168.0.1'
DNS_SERVER='192.168.0.1'
REMOTE_ADDR='whereischarlie.org'
REMOTE_PORT=80

class WifiController:
    def __init__(self):
        self._wlan = WLAN(mode=WLAN.STA)
        __configIf()
        __connectIf()
        __configSocket()

    def __configIf():
        _wlan.ifconfig(config=(ADDR, SUBNET_MASK, DEFAULT_GATEWAY, DNS_SERVER))

    def __connectIf():
        _wlan.connect(ssid='stranger', auth=(WLAN.WPA2, 'inastrangewlan'))
        while not _wlan.isconnected():
            time.sleep_ms(1000)

    def __configSocket():
        a = socket.getaddrinfo(REMOTE_ADDR, REMOTE_PORT)[0][-1]
        self._sock = socket.socket()
        _sock.connect(a)

    def canSend():
        """return true if interface can send data, false otherwise"""
        return _wlan.isconnected() and (s > 0)

    def send(data):
        """attempts to send via interface, returns success status"""
        _sock.send(data)
        return True
