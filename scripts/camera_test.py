#!/usr/bin/env python3 

import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
# import numpy as np

class Image_test:
    def __init__(self):
        rospy.init_node("wego_node")
        rospy.Subscriber("/usb_cam/image_rect_color/compressed", CompressedImage, self.image_CB)
        self.bridge = CvBridge()
        self.img_pub = rospy.Publisher("gray_color/compressed", CompressedImage, queue_size=5)

    def image_CB(self, data):
        # print(data)
        img = self.bridge.compressed_imgmsg_to_cv2(data)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        # img = cv2.imread("lane.jpg", cv2.IMREAD_COLOR)
        # img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # h, s, v = cv2.split(img_hsv)
        # lower_bound = np.array([0, 50, 0])
        # upper_bound = np.array([45, 255, 255])
        # img_inrange = cv2.inRange(img_hsv, lower_bound, upper_bound)
        cv2.line(img, (150,150), (300,300), (255,0,0), 3)
        
        cv2.imshow("image", img)
        cv2.waitKey(1)
        # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img_gray_msg = self.bridge.cv2_to_compressed_imgmsg(img_gray)
        
        cv_img_msg = self.bridge.cv2_to_compressed_imgmsg(img)
        self.img_pub.publish(cv_img_msg)

def main():
    image_test = Image_test()
    rospy.spin()

if __name__ == "__main__":
    main()