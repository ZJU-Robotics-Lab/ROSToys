import sys
import roslib
import rospy
import cv2
import os
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
from rosbag import Bag

with Bag('./HistoEQU.bag', 'w') as Y , Bag('./TrimmedStampedRenamedSynced.bag', 'r') as X :
    start_time = X.get_start_time()
    end_time = X.get_end_time()
    time_period = end_time - start_time
    cvbridge=CvBridge()
    for topic, msg, t in X:	
		time_for_now = float(t.secs)
		# print(time_for_now)
		# print(start_time)
		if topic == '/GroundCameraLeft/image_raw':
			header=msg.header
			before_histo = cvbridge.imgmsg_to_cv2(msg,'mono8')
			# creating a Histograms Equalization 
			# of a image using cv2.equalizeHist() 
			after_histo = cv2.equalizeHist(before_histo) 
			msg = cvbridge.cv2_to_imgmsg(after_histo, encoding='mono8')
			msg.header=header
			Y.write(topic, msg ,t)
		elif topic == '/GroundCameraRight/image_raw':
			header=msg.header
			before_histo = cvbridge.imgmsg_to_cv2(msg,'mono8')
			# creating a Histograms Equalization 
			# of a image using cv2.equalizeHist() 
			after_histo = cv2.equalizeHist(before_histo) 

			msg = cvbridge.cv2_to_imgmsg(after_histo, encoding='mono8')
			msg.header=header
			Y.write(topic, msg ,t)
		else :
			Y.write(topic, msg ,t)
		time = time_for_now-start_time
		# print(time)
		print(time/time_period)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

