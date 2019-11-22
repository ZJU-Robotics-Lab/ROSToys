from rosbag import Bag
import sys


with Bag('imageStamped1121_1.bag', 'w') as Y , Bag('./TrimedStampedRenamed.bag', 'r') as X :
    start_time = X.get_start_time()
    end_time = X.get_end_time()
    time_period = end_time - start_time
    cam0sequence = 0
    cam1sequence = 0
    timestamps=[]
    for (topic, msg, t) in X:

		time_for_now = float(t.secs)

		if topic == '/GroundCameraLeft/image_raw':
			msg.header.seq = cam0sequence
			timestamp=[]
			timestamp.append(msg.header.stamp.secs)
			timestamp.append(msg.header.stamp.nsecs)
			timestamps.append(timestamp)
			Y.write(topic, msg , t)
			cam0sequence += 1

			
		else :
			Y.write(topic, msg ,t)
		time = time_for_now-start_time
		print(time/time_period/2)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

    start_time = Y.get_start_time()
    end_time = Y.get_end_time()


with Bag('imageStamped1121_1.bag', 'r') as Y,  Bag('./out.bag', 'w') as W:
    for (topic, msg, t) in Y:

		time_for_now = float(t.secs)


		if topic == '/GroundCameraRight/image_raw':
			msg.header.seq = cam1sequence
			(msg.header.stamp.secs, msg.header.stamp.nsecs) = timestamps[cam1sequence]
			W.write(topic, msg , t)
			cam1sequence += 1

			
		else :
			W.write(topic, msg ,t)
		time = time_for_now-start_time
		print(time/time_period/2+0.5)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

