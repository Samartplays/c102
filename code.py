import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    #initialzing cv2
    videoCaptureObject = cs2.videoCaptureObject(0)
    result = True
    while(result):
        #read th frames while the camera is on
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("snapshot taken")

    videoCaptureObject.realease()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = ''
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read())
