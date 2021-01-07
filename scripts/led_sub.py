#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

def led1_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("1\n" if msg.data else "0\n")

def led2_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("3\n" if msg.data else "2\n")

def led3_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("5\n" if msg.data else "4\n")

def led4_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("7\n" if msg.data else "6\n")

def led5_callback(msg):
    with open("/dev/myled0", "w") as f:
        f.write("9\n" if msg.data else "8\n")

if __name__ == "__main__":
    rospy.init_node("led_flusher")
    sub1 = rospy.Subscriber("led1", Bool, led1_callback, queue_size=10)
    sub2 = rospy.Subscriber("led2", Bool, led2_callback, queue_size=10)
    sub3 = rospy.Subscriber("led3", Bool, led3_callback, queue_size=10)
    sub4 = rospy.Subscriber("led4", Bool, led4_callback, queue_size=10)
    sub5 = rospy.Subscriber("led5", Bool, led5_callback, queue_size=10)
    rospy.spin()
