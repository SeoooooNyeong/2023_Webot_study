#!/usr/bin/env python3 
#해쉬뱅을 작성함으로써 ROS에서 사용할 Python의 버전을 설정한다.

import rospy
from std_msgs.msg import Int32
#사용할 모듈을 입력한다.

rospy.init_node("wego_sub_node") # 1. 노드 작성

def callback(data):
    print(f"sub_data:{data}")
rospy.Subscriber("/counter", Int32, callback) #2. 노드의 역할을 설정
rospy.spin()