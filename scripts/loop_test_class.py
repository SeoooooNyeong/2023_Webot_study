#!/usr/bin/env python3 
#해쉬뱅을 작성함으로써 ROS에서 사용할 Python의 버전을 설정한다.

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from random import *

#사용할 모듈을 입력한다.
class Loop_test():
    def __init__(self):       
        rospy.init_node("wego_node") # 1. 노드 작성
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1) #2. 노드의 역할을 설정
        rospy.Subscriber("/turtle1/pose", Pose, self.callback) #2. 노드의 역할을 설정
        self.pub_data = Twist()
        self.sub_data = Pose()
        
    def callback(self, sub_data):
        if 1< sub_data.x <9 and 1<sub_data.y<9:
            self.pub_data.linear.x = random()*2
            self.pub_data.angular.z = random() *4 - 2
        else:
            self.pub_data.linear.x = 0.25
            self.pub_data.angular.z = 0.5
        print(f"sub_data:\n{sub_data}")
        print("-----------------------")
        self.pub.publish(self.pub_data) # 3. 토픽을 보내는 송신 시점 설정
        print(f"pub_data:\n{self.pub_data}")

def main():
    loop_test = Loop_test()        
    rospy.spin()

if __name__ == "__main__":
    main()