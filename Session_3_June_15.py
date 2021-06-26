import subprocess
import cv2

command = 'mkdir Video1Frames'
subprocess.call(command, shell=True)


# Function to extract frames
def frame_capture(path):
    # Path to video file
    vid_obj = cv2.VideoCapture(path)
    # Used as counter variable
    count = 0
    # check whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # extract frames
        success, image = vid_obj.read()
        # Save the frames with frame count
        cv2.imwrite("Video1Frames/video1_frame{}.jpg".format(count), image)
        count += 1
        if count == 10:
            break
        print(count)
    print("Loop ended")


# FrameCapture('Field Hockey Goalie Life.mp4')
# Driver code
if __name__ == '__main__':
    # Calling the function
    frame_capture('Field Hockey Goalie Life.mp4')
