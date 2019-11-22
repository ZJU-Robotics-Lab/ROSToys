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
                		if topic == "/GroundCameraLeft/image_raw": #topic for images；
                		        try:
                		            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                		        except CvBridgeError as e:
                		            print e
                		        timestr = "%.6f" %  msg.header.stamp.to_sec()
                		        #%.6fis the precision of the timestamps you prefer；
                		        image_name = timestr+ ".png" #name: timestamps.png
                		        cv2.imwrite(infra1_path + image_name, cv_image)  #save；
				if topic == "/GroundCameraRight/image_raw": 
                		        try:
                		            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                		        except CvBridgeError as e:
                		            print e
                		        timestr = "%.6f" %  msg.header.stamp.to_sec()

                		        image_name = timestr+ ".png" 
                		        cv2.imwrite(infra2_path + image_name, cv_image)  
				if topic == "/AeroCameraDown/color/image_raw":
                		        try:
                		            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                		        except CvBridgeError as e:
                		            print e
                		        timestr = "%.6f" %  msg.header.stamp.to_sec()
                		      
                		        image_name = timestr+ ".png" 
                		        cv2.imwrite(colorDown_path + image_name, cv_image)  
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
 

 
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
