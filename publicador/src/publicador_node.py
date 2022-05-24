#!/usr/bin/env python



import rospy
from std_msgs.msg import Int32







numero = Int32()



# MAIN
if __name__ == "__main__":

    alpha = 0


    rospy.init_node('nodo_publicador')
    
    rate = rospy.Rate(2)

    pub = rospy.Publisher('numeros', Int32, queue_size=1)

    while not(rospy.is_shutdown()):

        print("Introduce un numero entero: ")

        x = int(input())

        numero.data = x
        
        pub.publish(numero)

