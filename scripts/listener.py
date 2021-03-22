#!/usr/bin/python3
import rospy
from std_msgs.msg import String
#this is our callback
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "->I heard %s", data.data)
    
def listener():
 
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    #listener is our listener node time
    rospy.init_node('listener', anonymous=True)
    #this shows which topic we subscriber
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    flag=1 #here use for see difference of rospy.spin and roscpp::Spin
    if flag:
        rospy.spin()
    else:
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rate.sleep()
   
if __name__ == '__main__':
    listener()