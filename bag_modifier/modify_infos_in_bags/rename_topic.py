from rosbag import Bag
import sys


with Bag('./TrimedStampedRenamed.bag', 'w') as Y , Bag('./afterTrimedStamped.bag', 'r') as X :
    start_time = X.get_start_time()
    end_time = X.get_end_time()
    time_period = end_time - start_time
    for topic, msg, t in X:	
		time_for_now = float(t.secs)
		# print(time_for_now)
		# print(start_time)
		if topic == '/camera_array/cam0/image_raw':
			Y.write('/GroundCameraLeft/image_raw', msg ,t)
		elif topic == '/camera_array/cam1/image_raw':
			Y.write('/GroundCameraRight/image_raw', msg ,t)
		else :
			Y.write(topic, msg ,t)
		time = time_for_now-start_time
		# print(time)
		print(time/time_period)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

