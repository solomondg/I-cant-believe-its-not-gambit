#!/usr/bin/env python3

import numpy as np
import cv2

remote_ip = "127.0.0.1"
remote_port = 2898

current_packet = bytearray()
decoded_frame = None

x_resolution = 0
y_resolution = 0

stop = False

gotDescriptor = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((remote_ip, remote_port))

def listenForPackets():
    while not stop:
        current_packet, _ = sock.recvfrom(512)
        if len(current_packet) ==


def decodeDefFrame(frame):
    pass

def isDefFrame(frame);
