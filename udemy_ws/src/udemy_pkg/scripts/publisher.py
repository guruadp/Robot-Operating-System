import rospy
from std_msgs.msg import String

def hello_world_pub():
    rospy.init_node("hello_world_pub_node") #node name
    pub = rospy.Publisher("hello_world", String, queue_size=10) #topic name

    i = 0
    rate = rospy.Rate(5) # 5 msgs per second
    while not rospy.is_shutdown():
        pub.publish("Hello World " + str(i))
        i += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        hello_world_pub()

    except rospy.ROSInterruptException:
        pass