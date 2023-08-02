#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from math import pi


class Webot_control:
    def __init__(self):
        rospy.init_node("webot_node") #node 이름 정하기
        self.webot_ctrl_pub = rospy.Publisher("/commands/motor/speed", Float64, queue_size=1) # node 역할 정하기
        #queue size는 rostopic bw "토픽이름"으로 확인
        rospy.Subscriber("/scan", LaserScan, self.laser_CB)
        self.rate = rospy.Rate(10) # 주기 설정
        self.laser_msg = LaserScan()
        self.safe_range = 0.30
        
    def laser_CB(self, msg):
        # print(f"angle_min_dgree:{msg.angle_min*180/pi}")
        # print(f"angle_max_dgree:{msg.angle_max*180/pi}")
        # print(f"angle_increment_degree:{msg.angle_increment*180/pi}")
        # print(f"range_min:{msg.range_min}")
        # print(f"range_max:{msg.range_max}")
        # print(f"ranges:{msg.ranges}")
        print(f"---------------------")
        print(len(msg.ranges))
        degrees = [(msg.angle_min + msg.angle_increment * index)*180/pi for index, value in enumerate(msg.ranges)]
        num = 0
        
        for index, value in enumerate(msg.ranges):
            if 0 < value < self.safe_range and 150 < abs(degrees[index]):
                print(value)
                num += 1
            else:
                pass
            
        if num > 10:
            speed = 0
            print("stop")
        else:
            speed = 1000
            print("go")
        
        self.webot_ctrl_pub.publish(speed)
    
def main():
    webot_control = Webot_control()
    rospy.spin()

if __name__ == "__main__":
    main()