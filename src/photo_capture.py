#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naoqi import ALProxy

class PhotoCapture:

    def __init__(self, app):
        self.app = app
        self.photo = app.proxy["ALPhotoCapture"]

    def capture(self):
        self.photo.setPictureFormat("jpeg")
        self.photo.setResolution(2)
        self.photo.takePicture("/home/nao/recordings/cameras/", "image")
