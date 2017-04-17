#!/usr/bin/python3
from limitlessled.bridge import Bridge
from limitlessled.group.rgbw import RGBW
from limitlessled.group.white import WHITE
import time
import sys

bridge = Bridge('192.168.0.112',port=50000, version=1)
living_room=bridge.add_group(1, 'living_room', WHITE)
living_room.on = len(sys.argv) > 1 and sys.argv[1] == 'on'
time.sleep(2);
