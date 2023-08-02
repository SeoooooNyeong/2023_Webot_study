#!/usr/bin/env python3 
#해쉬뱅을 작성함으로써 ROS에서 사용할 Python의 버전을 설정한다.

import rospy
from geometry_msgs.msg import Twist

#사용할 모듈을 입력한다.
rospy.init_node("wego_pub_node") # 1. 노드 작성
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1) #2. 노드의 역할을 설정
rate = rospy.Rate(1)
data = Twist()


while not rospy.is_shutdown():
    data.angular.z = 1
    print(f"pub_data : {data}")
    pub.publish(data) # 3. 토픽을 보내는 송신 시점 설정
    rate.sleep()