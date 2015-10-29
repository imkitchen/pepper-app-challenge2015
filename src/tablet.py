# -*- coding : utf-8 -*-e
from naoqi import ALProxy


class PepperTablet:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        self.tablet = ALProxy("ALTabletService", self.ip_addr, self.port)

    def config_wifi(self, security, ssid, key):
        print self.tablet.configureWifi(security, ssid, key)

    def enable_wifi(self):
        self.tablet.enableWifi()

    def show_url(self, url):
        self.tablet.showWebview()
        self.tablet.loadUrl(url)


if __name__ == '__main__':
    tablet = PepperTablet("192.168.100.30", 9559)
    tablet.enable_wifi()
    tablet.tablet.cleanWebview()
    print tablet.tablet.getWifiStatus()
    tablet.show_url("http://html5test.com")
