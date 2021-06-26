import subprocess
import cv2

command = 'mkdir Video2Frames'
subprocess.call(command, shell=True)

vidcap = cv2.VideoCapture('Field Hockey Goalie Life.mp4')


def get_frame(start, frame_rate, termination_value):
    has_frames = 1
    count = 1
    while has_frames:
        # capturing to position in msec
        vidcap.set(cv2.CAP_PROP_POS_MSEC, start * 1000)
        has_frames, image = vidcap.read()
        print(has_frames)

        cv2.imwrite("Video2Frames/image_{}.jpg".format(count), image)
        count += 1
        start += frame_rate
        start = round(start, 2)
        print(count)

        if count == termination_value:
            break

    return has_frames


if __name__ == '__main__':
    get_frame(start=10, frame_rate=5, termination_value=15)
