#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Float64

class Webot_control:
    def __init__(self):
        rospy.init_node("webot_node") #node 이름 정하기
        self.webot_ctrl_pub = rospy.Publisher("/commands/motor/speed", Float64, queue_size=1) # node 역할 정하기
        #queue size는 rostopic bw "토픽이름"으로 확인
        self.rate = rospy.Rate(10) # 주기 설정
    
    def run(self):
        speed_msg = Float64()
        speed_msg.data = 1000
        self.webot_ctrl_pub.publish(speed_msg)

def main():
    webot_control = Webot_control()
    while not rospy.is_shutdown():
        webot_control.run()

if __name__ == "__main__":
    main()