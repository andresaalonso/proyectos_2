#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(mensaje):
    print("El mensaje recibido es :", mensaje)


rospy.init_node('suscriptor')
sus = rospy.Subscriber('numeros', Int32, callback=callback)



rospy.spin()