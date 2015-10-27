#!/usr/bin/env python

from naoqi import ALProxy
#from pepperazzi import

class PepperazziApp:
    def __init__(self, config):
        self.config = config
        #self.image_uploader = ImageUploader()

    def use(self, proxies):
        [ self.proxy. ALProxy(proxy) for proxy in proxies ]
                
    def run(self):
        return
        
#######################################

if __name__ == "__main__":
    app = PepperazziApp(ip, port)
    app.run()
