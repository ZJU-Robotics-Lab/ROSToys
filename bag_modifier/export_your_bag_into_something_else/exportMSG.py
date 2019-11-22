# coding:utf-8
#!/usr/bin/python

#Exrtact image from a bag file.

import roslib
import rosbag
import rospy
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

infra1_path = './Left/'
infra2_path = './Right/'
imu_data_path = './imuData/'
colorDown_path = './ColorDown/'
dji_imu_data_path = './dji_imuData/'


class ImageCreator():

	def __init__(self):
		self.bridge = CvBridge()
		with rosbag.Bag('./TrimmedStampedRenamedSynced.bag', 'r') as bag:
			for topic,msg,t in bag.read_messages():
                		if topic == "/GroundCameraLeft/image_raw": #图像的topic；
                		        try:
                		            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                		        except CvBridgeError as e:
                		            print e
                		        timestr = "%.6f" %  msg.header.stamp.to_sec()
                		        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                		        image_name = timestr+ ".png" #图像命名：时间戳.png
                		        cv2.imwrite(infra1_path + image_name, cv_image)  #保存；
				if topic == "/GroundCameraRight/image_raw": #图像的topic；
                		        try:
                		            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                		        except CvBridgeError as e:
                		            print e
                		        timestr = "%.6f" %  msg.header.stamp.to_sec()
                		        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                		        image_name = timestr+ ".png" #图像命名：时间戳.png
                		        cv2.imwrite(infra2_path + image_name, cv_image)  #保存；
				if topic == "/AeroCameraDown/color/image_raw": #图像的topic；
                		        try:
                		            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                		        except CvBridgeError as e:
                		            print e
                		        timestr = "%.6f" %  msg.header.stamp.to_sec()
                		        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                		        image_name = timestr+ ".png" #图像命名：时间戳.png
                		        cv2.imwrite(colorDown_path + image_name, cv_image)  #保存；
                		elif topic == "/mti/filter/orientation":
					timestr = "%.6f"% msg.header.stamp.to_sec()
					imu_data_name = timestr + ".txt"
					file = open(imu_data_path + imu_data_name, "w")
					message_string = str(msg)
					file.write(message_string)
                		elif topic == "/dji_sdk/imu":
					timestr = "%.6f"% msg.header.stamp.to_sec()
					imu_data_name = timestr + ".txt"
					file = open(dji_imu_data_path + imu_data_name, "w")
					message_string = str(msg)
					file.write(message_string)
if __name__ == '__main__':
 
    #rospy.init_node(PKG)
 
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
