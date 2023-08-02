#!/usr/bin/env python3 

#해쉬뱅을 작성함으로써 ROS에서 사용할 Python의 버전을 설정한다.

import rospy
from std_msgs.msg import Int32
#사용할 모듈을 입력한다.

class Pub_test:
    def __init__(self):
        rospy.init_node("wego_pub_node") # 1. 노드 작성
        self.pub = rospy.Publisher("/counter", Int32, queue_size=1) #2. 노드의 역할을 설정
        self.rate = rospy.Rate(1)
        self.data = 0

    def pub_fn(self):
        while not rospy.is_shutdown():
            self.data += 1
            print(f"pub_data :{self.data}")
            self.pub.publish(self.data) # 3. 토픽을 보내는 송신 시점 설정
            self.rate.sleep()

def main():
    pub_data = Pub_test()
    pub_data.pub_fn()

if __name__ == "__main__":
    main()