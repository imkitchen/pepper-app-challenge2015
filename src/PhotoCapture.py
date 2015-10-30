#!/usr/bin/env python
import datetime
from naoqi import ALProxy

photo = ALProxy("ALPhotoCapture", "192.168.10.74", 9559)
photo.setPictureFormat("jpeg")
photo.setResolution(4)
photo.takePicture("/home/nao/recordings/cameras/", str(datetime.datetime.today()))
