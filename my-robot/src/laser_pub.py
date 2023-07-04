#!/usr/bin/env python3
# license removed for brevity
import rospy
from sensor_msgs.msg import LaserScan

def talker(data):
    pub = rospy.Publisher('scan2', LaserScan, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo("scan2 published")
        pub.publish(data)

def callback(data):
    data.ranges = data.ranges[10:]
    talker(data)
    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("scan", LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()