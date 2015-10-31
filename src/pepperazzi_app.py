#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from argparse import ArgumentParser
from naoqi    import ALProxy

class PepperazziApp:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port    = port
        self.proxy   = []
        self.watcher = []

    def inject(self, proxies):
        for proxy in proxies:
            self.proxy[proxy] = ALProxy(proxy, self.ip_addr, self.port)

    # TODO:
    def watch(self, watcher):
        pass
            
    def run(self):
        print("pepper IP adress: " + self.ip_addr)
        print("port number: " + self.port)
        
    @staticmethod
    def main():
        parser = ArgumentParser()

        parser.add_argument("-i", "--ip_addr",
                            dest    = "ip_addr",
                            type    = str,
                            default = "127.0.0.1",
                            help    = "PepperのIPアドレス")
        
        parser.add_argument("-p", "--port",
                            dest    = "port",
                            type    = int,
                            default = 9559,
                            help    = "ポート番号")
        
        args = parser.parse_args()
        app  = PepperazziApp(args.ip_addr, args.port)
        app.inject([
            "ALMotion",
            "ALTextToSpeech",
            "ALPhotoCapture",
        ])
        app.run()

#######################################
    
if __name__ == "__main__":
    PepperazziApp.main()
