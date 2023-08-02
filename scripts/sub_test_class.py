#!/usr/bin/env python3 
#해쉬뱅을 작성함으로써 ROS에서 사용할 Python의 버전을 설정한다.

import rospy
from std_msgs.msg import Int32
#사용할 모듈을 입력한다.

class Sub_test:
    def __init__(self):
        rospy.init_node("wego_pub_node")
        self.sub = rospy.Subscriber("/counter", Int32, self.callback) #2. 노드의 역할을 설정

    def callback(self , data):
        print(f"sub_data:{self, data}")

def main():
    sub_test = Sub_test()
    rospy.spin()

if __name__ == "__main__":
    main()