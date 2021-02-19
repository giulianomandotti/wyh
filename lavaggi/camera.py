import cv2
import keyboard

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        retlist = [jpeg.tobytes(), image]
        return retlist


def gen(camera):
    FILE_OUTPUT = 'output.mp4'
    # Get current width of frame
    width = camera.video.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    # Get current height of frame
    height = camera.video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(FILE_OUTPUT, fourcc, 20.0, (int(width), int(height)))

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
            frame = camera.get_frame()[0]
            saveframe = camera.get_frame()[1]
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            out.write(saveframe)
             
            # if cv2.waitKey(1) & 0xFF == ord('a'):
            #    break
            
            if keyboard.is_pressed('x'):
                break
