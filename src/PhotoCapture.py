#!/usr/bin/env python

from naoqi import ALProxy

photo = ALProxy("ALPhotoCapture", "163.221.68.225", 9559)
photo.setPictureFormat("jpeg")
photo.setResolution(4)
photo.takePicture("/home/nao/recordings/cameras/", "image")
