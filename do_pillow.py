#!/usr/bin/env python3
#coding:utf-8
from PIL import Image
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thum.jpg', 'JPEG')
print(im.format, im.size, im.mode)
