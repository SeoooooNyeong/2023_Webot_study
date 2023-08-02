#!/usr/bin/env python3 
#해쉬뱅을 작성함으로써 ROS에서 사용할 Python의 버전을 설정한다.

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

#사용할 모듈을 입력한다.

rospy.init_node("wego_node") # 1. 노드 작성

pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1) #2. 노드의 역할을 설정
pub_data = Twist()
sub_data = Pose()
pub_data.linear.x = 1
def callback(sub_data):
    if sub_data.x <9:
        pub_data.linear.x = 1
    else:
        pub_data.linear.x = 0
    
    pub.publish(pub_data) # 3. 토픽을 보내는 송신 시점 설정

    print(f"sub_data:\n{sub_data}")
    
rospy.Subscriber("/turtle1/pose", Pose, callback) #2. 노드의 역할을 설정
rospy.spin()