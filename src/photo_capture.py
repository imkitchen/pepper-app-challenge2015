#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naoqi import ALProxy

photo = ALProxy("ALPhotoCapture", "163.221.68.225", 9559)
photo.setPictureFormat("jpeg")
photo.setResolution(2)
photo.takePicture("/home/nao/recordings/cameras/", "image")
