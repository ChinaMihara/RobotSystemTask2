#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
    rospy.init_node("led_pub")
    pub1 = rospy.Publisher("led1", Bool, queue_size=10)
    pub2 = rospy.Publisher("led2", Bool, queue_size=10)
    pub3 = rospy.Publisher("led3", Bool, queue_size=10)
    pub4 = rospy.Publisher("led4", Bool, queue_size=10)
    pub5 = rospy.Publisher("led5", Bool, queue_size=10)
    
    rate= rospy.Rate(10)

    pub1.publish(False)
    pub2.publish(False)
    pub3.publish(False)
    pub4.publish(False)
    pub5.publish(False)
    
    try:
        while not rospy.is_shutdown():
            direction = input('r:Red  y:Yellow  g:Green  b:Blue  w:White  E:Erase>>  ')
            if 'r' in direction:
                pub1.publish(True)
                pub2.publish(False)
                pub3.publish(False)
                pub4.publish(False)
                pub5.publish(False)

            if 'y' in direction:
                pub1.publish(False)
                pub2.publish(True)
                pub3.publish(False)
                pub4.publish(False)
                pub5.publish(False)

            if 'g' in direction:
                pub1.publish(False)
                pub2.publish(False)
                pub3.publish(True)
                pub4.publish(False)
                pub5.publish(False)

            if 'b' in direction:
                pub1.publish(False)
                pub2.publish(False)
                pub3.publish(False)
                pub4.publish(True)
                pub5.publish(False)

            if 'w' in direction:
                pub1.publish(False)
                pub2.publish(False)
                pub3.publish(False)
                pub4.publish(False)
                pun5.publish(True)

            if 'E' in direction:
                pub1.publish(False)
                pub2.publish(False)
                pub3.publish(False)
                pub4.publish(False)
                pub5.publish(False)

                rate.sleep()

    except rospy.KeybordInterrupt:
            pub1.publish(False)
            pub2.publish(False)
            pub3.publish(False)
            pub4.publish(False)
            pub5.publish(False)
            pass

    
