from rosbag import Bag
import sys


with Bag('imageStamped1121_1.bag', 'w') as Y , Bag('./1121before.bag', 'r') as X :
    start_time = X.get_start_time()
    end_time = X.get_end_time()
    time_period = end_time - start_time
    for topic, msg, t in X:
		tCam1 = t	
		time_for_now = float(t.secs)
		# print(time_for_now)
		# print(start_time)
		if topic == '/camera_array/cam1/image_raw':
			tCam1.secs = t.secs+1574323871-1574323885
			tCam1.nsecs = t.nsecs + 507150156 - 973867862
			if tCam1.nsecs <= 0:
				tCam1.nsecs += 1000000000
				tCam1.secs -= 1
			if tCam1.nsecs >= 1000000000:
				tCam1.nsecs -= 1000000000
				tCam1.secs += 1
			msg.header.stamp.secs = tCam1.secs
			msg.header.stamp.nsecs = tCam1.nsecs
			#print("Cam1:") 
			#print(tCam1.secs,tCam1.nsecs,"       ",t.secs, t.nsecs,"    ",msg.header.stamp.secs,msg.header.stamp.nsecs)
			Y.write(topic, msg ,tCam1)
			
		else :
			Y.write(topic, msg ,t)
			#print("Others",t.secs, t.nsecs)
		time = time_for_now-start_time
		print(time/time_period)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

