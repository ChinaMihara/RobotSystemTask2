#!/usr/bin/env python3
#SPDX-License-Identifier: GPL-3.0
#
#Copyright (C) 2021 China Mihara + Yuki Iida. All rights reserved.

import rospy
from std_msgs.msg import Bool

def led_red_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("1\n" if msg.data else "0\n")

def led_yellow_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("3\n" if msg.data else "2\n")

def led_green_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("5\n" if msg.data else "4\n")

def led_blue_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("7\n" if msg.data else "6\n")

def led_white_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("9\n" if msg.data else "8\n")

if __name__ == "__main__":
    rospy.init_node("led_flusher")
    sub1 = rospy.Subscriber("led_red", Bool, led1_callback, queue_size=10)
    sub2 = rospy.Subscriber("led_yellow", Bool, led2_callback, queue_size=10)
    sub3 = rospy.Subscriber("led_green", Bool, led3_callback, queue_size=10)
    sub4 = rospy.Subscriber("led_blue", Bool, led4_callback, queue_size=10)
    sub5 = rospy.Subscriber("led_white", Bool, led5_callback, queue_size=10)
    rospy.spin()
